const RouteOption = require('../models/routeOption.model');

exports.getRouteOptions = async (req, res, next) => {
    try {
        const routeOptions = await RouteOption.findAll();
        res.json(routeOptions);
    } catch (error) {
        next(error);
    }
}