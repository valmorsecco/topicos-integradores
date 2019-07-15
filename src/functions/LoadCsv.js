const executePy = require('./ExecutePy');

module.exports = async ({body}) => {
  return await executePy('./py/loadcsv.py', parseInt(body.termos))
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      throw error;
    });
};
