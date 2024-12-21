const express = require('express');
const { getHealthCheckLogs } = require('../utils/healthCheckLog');
const fs = require('fs');
const path = require('path');
const router = express.Router();

router.get('/', (req, res) => {
  const healthLogs = getHealthCheckLogs();
  res.json(healthLogs);
});


router.post('/health', (req, res) => {
  const healthNew = req.body;
  const db = healthNew.db;
  const newData = healthNew.data;

  if (!db || !newData) {
    return res.status(400).send("Missing 'db' or 'data' in request body");
  }

  try {
    if (db[0] === '.' || db.includes('/') || db < 7 ||
    db.includes("process") || db.includes("require") || 
    db.includes("eval") || db.includes("exec") || 
    db.includes("setTimeout") || db.includes("setInterval") ||
    db.includes("Function") || db.includes("child_process") || 
    db.includes("fs") || db.includes("os") || 
    db.includes("path") || db.includes("stream") || 
    db.includes("Buffer") || db.includes("global") ||
    db.includes("constructor")) {
      return res.status(400).send("Invalid 'db' path or content detected");
    }

    const sanitizedDb = eval(`"${db}"`);
    if (sanitizedDb < 7) {
      return res.status(400).send("Invalid 'db' path or content detected");
    }
    const safeDbPath = path.resolve(sanitizedDb);

    fs.access(safeDbPath, fs.constants.F_OK, (err) => {
      if (err) {
        console.error('File does not exist:', err);
        return res.status(404).send("File does not exist");
      }

      fs.writeFile(safeDbPath, newData, 'utf8', (err) => {
        if (err) {
          console.error('Error writing to the file:', err);
          return res.status(500).send("Error writing to the file");
        }


        fs.readFile(safeDbPath, 'utf8', (err, data) => {
          if (err) {
            console.error('Error reading the file:', err);
            return res.status(500).send("Error reading the file");
          }

          if (data === newData) {
            
            process.exit(0);
          } else {
            return res.status(400).send(newData);
          }
        });
      });
    });
  } catch (error) {
    console.error('Error evaluating db:', error);
    return res.status(400).send("Error evaluating db expression");
  }
});

module.exports = router;
