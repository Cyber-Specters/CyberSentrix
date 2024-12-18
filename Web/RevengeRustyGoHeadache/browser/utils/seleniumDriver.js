const { Builder, Browser } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const { updateHealthCheck } = require('./healthCheckLog');
const axios = require('axios');
const { isSSRFSafeURL } = require('ssrfcheck');
const { localUrl, remoteDebuggingPort, seleniumOptions } = require('../config/appConfig');

async function setupWebDriver() {
  const options = new chrome.Options();
  options.addArguments(`--remote-debugging-port=${remoteDebuggingPort}`);
  seleniumOptions.forEach(option => options.addArguments(option));

  return new Builder()
    .forBrowser(Browser.CHROME)
    .setChromeOptions(options)
    .build();
}

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000)); 
}

async function navigateToPage(driver, url) {
  console.log(`Navigating to: ${url}`);
  await driver.get(url);
  await sleep(10);
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
    await navigateToPage(driver, url);
    console.log('Closing WebDriver session after page is loaded.');
    await driver.quit();
  } catch (error) {
    updateHealthCheck('fail');
    console.error('Error:', error.message);
  }
  if (driver) {
    await driver.quit();
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
  if (!isSSRFSafeURL(url)) {
    updateHealthCheck('fail');
    new Error(`URL "${url}" is not safe for SSRF.`);
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
