const express = require('express');
const router = express.Router();

const AjustarMatrizUseCase = require('../actions/AjustarMatriz.js');

router.post('/ajustar-matriz', async (req, res, next) => {
  const ajustarMatrizUseCase = new AjustarMatrizUseCase();
  const {
    ERROR,
    SUCCESS,
  } = ajustarMatrizUseCase.outputs;

  ajustarMatrizUseCase.on(ERROR, next).on(SUCCESS, data => {
    res.status(200).json(data);
  });

  ajustarMatrizUseCase.execute({body: req.body});
});

module.exports = app => app.use('/py', router);
