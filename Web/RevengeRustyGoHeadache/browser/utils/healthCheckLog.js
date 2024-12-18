let total_health_check = [];

function updateHealthCheck(status) {
  const options = {
    timeZone: 'Asia/Jakarta',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    year: 'numeric',
    month: 'numeric',
    day: 'numeric',
  };

  const jakartaTime = new Intl.DateTimeFormat('en-US', options).format(new Date());
  
  total_health_check.push({ time: jakartaTime, status: status });
  console.log('Health check updated:', { time: jakartaTime, status: status });
}

function getHealthCheckLogs() {
    return total_health_check.slice(-20);
}

module.exports = { updateHealthCheck, getHealthCheckLogs };
