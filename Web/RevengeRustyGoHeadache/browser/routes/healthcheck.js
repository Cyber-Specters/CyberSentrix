const express = require('express');
const { getHealthCheckLogs } = require('../utils/healthCheckLog');

const router = express.Router();

router.get('/', (req, res) => {
  const healthLogs = getHealthCheckLogs();
  res.json(healthLogs);
});

module.exports = router;
