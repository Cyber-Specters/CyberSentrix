require('dotenv').config(); 

const express = require('express');
const healthcheckRoutes = require('./routes/healthcheck');
const { startHealthCheckCron } = require('./utils/cronjob');

const app = express();

const PORT = process.env.PORT || 3000;

app.use(express.json()); 


app.use('/healthcheck', healthcheckRoutes);

startHealthCheckCron();

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
