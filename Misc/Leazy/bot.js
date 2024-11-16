const { generateSync } = require("text-to-image");
const realip = require("request-ip");
const Crypto = require("crypto")
const fs = require("fs");
const path = require("path");
const express = require("express");
const DEFUALT_START = "PNG";
const DEFAULT_END = "IHDR";
const app = express();
app.use(realip.mw());
const port = process.env.PORT || 3001;
const FLAG = process.env.FLAG || "FLAG{EASY_CHALL_FAKEFLAG}";
const dataUri = generateSync(FLAG, {
  maxWidth: 220,
  customHeight: 220,
  fontSize: 11,
  textAlign: "center",
  verticalAlign: "center",
});

const AUTHORIZED_IP = process.env.AUTHORIZED_IP || "::ffff:127.0.0.1";

function startToEnd(stORend) {
  var my_pleasure = "";
  for (var positionx = 0; positionx < stORend.length; positionx++) {
    if (stORend.charCodeAt(positionx) <= 127) {
      my_pleasure += stORend.charAt(positionx);
    }
  }
  return my_pleasure;
}

function rInBUF(buffer, st, end) {
  const sb = Buffer.from(st);
  const rb = Buffer.from(end);

  if (rb.length !== sb.length) {
    throw new Error(`Error`);
  }

  let index = buffer.indexOf(sb);

  while (index !== -1) {
    buffer.set(rb, index);
    index = buffer.indexOf(sb, index + sb.length);
  }

  return buffer;
}

function genFlag(start, end) {
  let buffer = Buffer.from(dataUri.split(",")[1], "base64");
  try {
    if (
      DEFUALT_START.toLowerCase().includes(start.toLowerCase()) ||
      DEFAULT_END.toLowerCase().includes(end.toLowerCase())
    ) {
      return console.error("Not must be same as the default start or end");
    }
    buffer = rInBUF(buffer, startToEnd(DEFUALT_START),startToEnd(start));
    buffer = rInBUF(buffer, startToEnd(DEFAULT_END), startToEnd(end));
    fs.writeFile(tmpFile, buffer, (err) => {
      if (err) {
        console.error("Error write idk why tho : ", err);
      } 
    });
  } catch (error) {
    console.error("Error processing buffer:", error.message);
  }
}


app.get("/render", (req, res) => {
  tmpFile = path.join(__dirname, `${Crypto.randomBytes(6).readUIntLE(0, 6).toString(36)}.png`);

  realclientIp = req.clientIp;
  if (realclientIp === AUTHORIZED_IP) {
    ctyp = req.query.ct;
  }
  realclientip = req.socket.remoteAddress;
  if (realclientip !== AUTHORIZED_IP) {
    console.log(realclientip);
    res.status(401).send("Unauthorized");
    return;
  } 
  const download = req.query.download;

  if (download === "true") {
    res.send(dataUri);
  } else if (download === "false") {
    if (req.query.start && req.query.end) {
      genFlag(req.query.start, req.query.end);
    }
    fs.readFile(tmpFile, (err, buffer) => {
      if (err) {
        res.status(500).send("we cant open the file");
      } else {
        res.writeHead(200, {
          "Content-Type": ctyp || "notsetted",
          "Content-Length": buffer.length,
        });
        res.end(buffer, () => {
          fs.unlink(tmpFile, (unlinkErr) => {
            if (unlinkErr) {
              console.error("something error when delet");
            }
          });
        });
      }
    });
  } else {
    res.send("He127.l.l.0day World!");
  }
});

app.listen(port, () => {
  console.log(`authorized ip : ${AUTHORIZED_IP}`);
  console.log(`Example app listening on port ${port}`);
});
