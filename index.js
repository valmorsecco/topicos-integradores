const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

require('./src/controllers/pyController.js')(app);

app.listen(3000, () => {
  console.log('APP: localhost:3000');
});
