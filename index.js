const express = require('express');
const app = express();
const csv = require('csv-parser');
const fs = require('fs');
const { spawn } = require('child_process');

const org = [];

const loadValues = () => {
  executePy('./py/corrcoef.py');
  // fs.createReadStream('./csv/data.csv')
  //   .pipe(csv())
  //   .on('data', (row) => {
  //     let values = Object.values(row);
  //     for(var i = 0; i < values.length; i++) {
  //       values[i] = parseFloat(values[i]);
  //     }
  //     org.push(values);
  //   })
  //   .on('end', () => {
  //     executePy('./py/corrcoef.py', JSON.stringify(org));
  //   });
};

const executePy = (file) => {
  const pyProg = spawn('python', [file]);
  pyProg.stdout.on('data', function(data) {
    console.log(data.toString());
  });
}

loadValues();

app.listen(3000, () => {
  console.log('Listen localhost:3000')
});
