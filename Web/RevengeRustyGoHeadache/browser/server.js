require('dotenv').config(); 

const express = require('express');
const healthcheckRoutes = require('./routes/healthcheck');
const { startHealthCheckCron } = require('./utils/cronjob');

const app = express();

const PORT = process.env.PORT || 3001;

app.use(express.json()); 

console.log('DEBUG is:', process.env.DEBUG);
app.use('/healthcheck', healthcheckRoutes);

startHealthCheckCron();

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});