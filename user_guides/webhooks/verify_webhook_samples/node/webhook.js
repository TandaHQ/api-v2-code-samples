//
// npm init
// npm install express body-parser
// node webhook.js
//

const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const util = require('util');

const ap = (data) => console.log(util.inspect(data, { colors: true, depth: null }));

const app = express();
const port = 3000;
const securityToken = 'tandawebhooktest';

app.use(bodyParser.json());

app.post('/', (req, res) => {
  const payload = req.body.payload;
  const signature = req.headers['x-hook-signature'];
  const actualSignature = crypto.createHmac('sha1', securityToken).update(JSON.stringify(payload)).digest('hex');

  ap(`Signature: ${signature}`);
  ap(`Actual Signature: ${actualSignature}`);

  ap(payload);

  res.status(204).send();
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
