const cron = require('node-cron');
const { bot } = require('./seleniumDriver');  

function startHealthCheckCron() {
  cron.schedule('*/7 * * * * *', async () => {
    console.log('Checking localhost:3000...');
    await bot();
    await new Promise(resolve => setTimeout(resolve, 3000));  
  });
}

module.exports = { startHealthCheckCron };
