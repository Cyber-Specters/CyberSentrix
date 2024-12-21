const cron = require('node-cron');
const { bot } = require('./seleniumDriver');  
const fs = require('fs');


function resetEnv() {
  const envContent = `
PORT=3001
FLAG=lastchallfrommethischallcreatedonlyfor1days?sorryfurrushchall.dontsubmitthis
DEBUG=false
  `;

  fs.writeFileSync('.env', envContent, 'utf8');
  console.log('.env file has been reset successfully');
}

function startHealthCheckCron() {
  cron.schedule('*/3 * * * * *', async () => {
    console.log('Checking localhost:3000...');
    await bot();
    // sleep(10);
    resetEnv();

  });
}

module.exports = { startHealthCheckCron };
