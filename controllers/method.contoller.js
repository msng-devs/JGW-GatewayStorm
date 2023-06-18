const Method = require('../models/method.model');

exports.getMethods = async (req, res, next) => {
    try {
        const methods = await Method.findAll();
        res.json(methods);
    } catch (error) {
        next(error);
    }
}