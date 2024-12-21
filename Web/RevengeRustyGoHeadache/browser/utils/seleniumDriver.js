const { Builder, Browser } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const { updateHealthCheck } = require('./healthCheckLog');
const axios = require('axios');
const { isSSRFSafeURL } = require('ssrfcheck');
const { localUrl, remoteDebuggingPort, seleniumOptions } = require('../config/appConfig');

async function setupWebDriver() {
  const service = new chrome.ServiceBuilder()
    .setPort(6969)
  
  const options = new chrome.Options();
  options.addArguments(`--remote-debugging-port=${remoteDebuggingPort}`);
  options.addArguments(`--remote-debugging-address=127.0.0.1`);
  seleniumOptions.forEach(option => options.addArguments(option));
  return new Builder()
    .forBrowser('chrome')
    .setChromeOptions(options)
    .setChromeService(service)
    .build();
}



async function navigateToPage(driver, url) {
  console.log(`Navigating to: ${url}`);
  await driver.get(url);
  await driver.sleep(2000);
  console.log('Page loaded successfully.');
  updateHealthCheck('ok');
}

async function bot() {
  const url = 'http://localhost:3000';  
  let driver;

  try {
    await validateUrl(url);
    await checkUrlSecurity(url);

    driver = await setupWebDriver();
    if (driver) {
      await navigateToPage(driver, url);

    }
    console.log('Closing WebDriver session after page is loaded.');
  } catch (error) {
    updateHealthCheck('fail');
    console.error('Error:', error);
  } finally {
    if (driver) {
      await driver.quit();
    }
  }

}

function validateUrl(url) {
  const bannedPatterns = [/192\.168\.\d+\.\d+/, /\/sessions/i];
  if (bannedPatterns.some((pattern) => pattern.test(url))) {
    updateHealthCheck('fail');
    throw new Error(`Access to the URL "${url}" is prohibited due to security restrictions.`);
  }
}

async function checkUrlSecurity(url) {
  if (process.env.DEBUG != "true"){
    if (!isSSRFSafeURL(url)) {
      updateHealthCheck('fail');
      throw new Error(`URL "${url}" is not safe for SSRF.`);
    }
  }
  const response = await axios.get(url, { timeout: 5000 });
  const hostHeader = response.request.getHeaders().host;
  if (hostHeader.includes('/session')) {
    updateHealthCheck('fail');
    throw new Error(`Access to the URL "${url}" is prohibited due to security restrictions.`);
  }
  console.log(`URL and host header validated successfully: ${hostHeader}`);
}

module.exports = { bot };
