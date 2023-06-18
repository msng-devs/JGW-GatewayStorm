const ApiRoute = require('../models/apiRoute.model');
const assert = require("assert");
const ApplicationException = require("../utlis/exception/application.exception");
const ApplicationErrorCode = require("../utlis/exception/application.exception");

exports.getApiRoute = async (req, res, next) => {
    try {
        const apiRoute = await ApiRoute.findByPk(req.params.id);
        assert(apiRoute)
        res.json(apiRoute);
    } catch (error) {
        if (error instanceof assert.AssertionError) throw ApplicationException(ApplicationErrorCode.NOT_FOUND,"Api Route not found");
        next(error);
    }
};

exports.createApiRoute = async (req, res, next) => {
    try {
        const apiRoute = await ApiRoute.create(req.body);
        res.json(apiRoute);
    } catch (error) {
        next(error);
    }
}

exports.findApiRouteById = async (req, res, next) => {
    try {
        const apiRoute = await ApiRoute.findByPk(req.params.id);
        assert(apiRoute)
        res.json(apiRoute);
    } catch (error) {
        if (error instanceof assert.AssertionError) throw ApplicationException(ApplicationErrorCode.NOT_FOUND,"Api Route not found");
        next(error);
    }
}

exports.findApiRouteByServiceId = async (req, res, next) => {
    try {
        const apiRoute = await ApiRoute.findAll({
            where: {
                serviceId: req.params.serviceId
            }
        });
        res.json(apiRoute);
    } catch (error) {
        next(error);
    }
}

exports.updateApiRoute = async (req, res, next) => {
    try {
        const apiRoute = await ApiRoute.findByPk(req.params.id);
        assert(apiRoute)
        await apiRoute.update(req.body);
        res.json(apiRoute);

    } catch (error) {
        if (error instanceof assert.AssertionError) throw ApplicationException(ApplicationErrorCode.NOT_FOUND,"Api Route not found");
        next(error);
    }
}

exports.deleteApiRoute = async (req, res, next) => {
    try {
        const apiRoute = await ApiRoute.findByPk(req.params.id);
        assert(apiRoute)

        await apiRoute.destroy();
        res.status(204).end();

    } catch (error) {
        if (error instanceof assert.AssertionError) throw ApplicationException(ApplicationErrorCode.NOT_FOUND,"Api Route not found");
        next(error);
    }
}