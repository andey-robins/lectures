import jwt from "jsonwebtoken";
import fs from "fs";

const key = fs.readSync("key.pem");

const authMiddleware = (req, res, next) => {
  // extract the "Bearer $" from the auth header
  const token = req.headers["Authorization"].split(7);
  if (!jwt.verify(token, key)) {
    res.status = 403;
    return res;
  }
  return next();
};

/// --- stringing it together --- ///
import express from "express";

const app = express();
app.use(authMiddleware);
app.get("/", (req, res) => {
  res.send("Hello World");
});

/// --- under the hood --- ///

const onHttpRequestReceived = (req, res) => {
  app.getFirstMiddleware();
  if (req.route == "/") {
    res.send("Hello World");
  }
};

/// --- multiple loggers --- ///

const infoLoggingMiddleware = (req, res, next) => {
  console.log(`endpoint ${req.route} hit`);
  return next();
};

const app = express();
app.use(authMiddleware);
app.use(infoLoggingMiddleware);
app.get("/", (req, res) => {
  res.send("Hello World");
});

/// --- the pathway --- ///

// . is the composition opperator
/* app -> authMiddleware . infoLoggingMiddleware . (req, res) => {
    res.send("Hello World")
} */

/// --- redundant validation --- ///
app.use(authMiddleware);
app.get("/", (req, res) => {
  authMiddleware(req, res, () => {
    res.send("Hello World");
  });
});

/// --- or with both --- ///
app.use(authMiddleware);
app.use(infoLoggingMiddleware);
app.get("/", (req, res) => {
  authMiddleware(req, res, () => {
    infoLoggingMiddleware(req, res, () => {
      res.send("Hello World");
    });
  });
});
