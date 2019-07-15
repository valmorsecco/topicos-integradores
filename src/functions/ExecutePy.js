const {spawn} = require('child_process');

module.exports = (file, ...args) => {
  return new Promise((resolve, reject) => {
    const pyProg = spawn('python', [file, ...args]);
    pyProg.stdout.on('data', data => {
      resolve(data.toString());
    });
    pyProg.on('error', error => {
      reject(error);
    });
    pyProg.on('uncaughtException', error => {
      reject(error);
    });
    pyProg.stderr.on('data', error => {
      reject(error);
    });
  });
};
