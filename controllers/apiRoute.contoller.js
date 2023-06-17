const ApiRoute = require('../models/apiRoute.model');

exports.getApiRoute = async (req, res, next) => {
    try {
        const apiRoute = await ApiRoute.findByPk(req.params.id);
        res.json(apiRoute);
    } catch (error) {
        next(error);
    }
};