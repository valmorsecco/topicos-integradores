const Operation = require('./Operation');

const LoadCsv = require('./../functions/LoadCsv');

class AjustarMatriz extends Operation {
  constructor() {
    super();
  }

  async execute({body}) {
    const {
      ERROR,
      SUCCESS,
    } = this.outputs;

    try {
      await LoadCsv({body});
      return this.emit(SUCCESS, {
        success: 'Success',
      });
    } catch (error) {
      this.emit(ERROR, {
        error: 'Error',
      });
    }
  }
}

AjustarMatriz.setOutputs(['ERROR', 'SUCCESS']);

module.exports = AjustarMatriz;
