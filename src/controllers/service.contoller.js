const Service = require('../models/service.model');
const {createPage} = require("/src/utlis/pagenation");
const ApplicationException = require("../utlis/exception/application.exception");
const ApplicationErrorCode = require("../utlis/exception/application.exception");
const assert = require("assert");

exports.getServices = async (req, res, next) => {
    try {
        const page = createPage(req);
        const services = await Service.findAll({
            offset: page.offset,
            limit: page.limit,
            order: [['id', 'DESC']]
        });
        res.json(services);
    } catch (error) {
        next(error);
    }
};

exports.createService = async (req, res, next) => {
    try {
        const service = await Service.create(req.body);
        res.json(service);
    } catch (error) {
        next(error);
    }
}

exports.findServiceById = async (req, res, next) => {
    try {
        const service = await Service.findByPk(req.params.id);
        assert (service);
        res.json(service);
    } catch (error) {
        if (error instanceof assert.AssertionError) throw ApplicationException(ApplicationErrorCode.NOT_FOUND,"Service not found");
        next(error);
    }
}

exports.updateService = async (req, res, next) => {
    try {
        const service = await Service.findByPk(req.params.id);
        assert(service);
        await service.update(req.body);
        res.json(service);

    } catch (error) {
        if (error instanceof assert.AssertionError) throw ApplicationException(ApplicationErrorCode.NOT_FOUND,"Service not found");
        next(error);
    }
}

exports.deleteService = async (req, res, next) => {
    try {
        const service = await Service.findByPk(req.params.id);
        assert(service);

        await service.destroy();
        res.status(204).end();

    } catch (error) {
        if (error instanceof assert.AssertionError) throw ApplicationException(ApplicationErrorCode.NOT_FOUND,"Service not found");
        next(error);
    }
}