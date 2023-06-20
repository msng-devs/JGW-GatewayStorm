const Service = require('../models/service.model');
const {createPage} = require("../utlis/pagenation");
const {ApplicationException, ApplicationErrorCode} = require("../utlis/exception/application.exception");

exports.getServices = async (req, res, next) => {
    const page = createPage(req);
    const services = await Service.findAll({
        offset: page.offset, limit: page.limit, order: [['id', 'DESC']]
    });
    res.json(services.map(serviceToJson));
};

exports.createService = async (req, res, next) => {
    await checkUnique(req.body.name, req.body.domain);
    const service = {
        name: req.body.name, domain: req.body.domain, index: req.body.index
    }
    const newService = await Service.create(service);
    res.json(serviceToJson(newService));
}

exports.findServiceById = async (req, res, next) => {

    const service = await Service.findByPk(req.params.id);
    if (!service) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "해당 서비스를 찾을 수 없습니다.");
    res.json(serviceToJson(service));

}

exports.updateService = async (req, res, next) => {

    const service = await Service.findByPk(req.params.id);
    if (!service) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "해당 서비스를 찾을 수 없습니다.");
    await checkUnique(req.body.name, req.body.domain)

    await service.update({
        name: req.body.name, domain: req.body.domain, index: req.body.index
    });
    res.json(serviceToJson(service));

}

exports.deleteService = async (req, res, next) => {

    const service = await Service.findByPk(req.params.id);
    if (!service) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "해당 서비스를 찾을 수 없습니다.");

    await service.destroy();
    res.status(204).end();

}

const checkUnique = async (name, domain) => {
    const serviceDomain = await Service.findOne({
        where: {
            domain: domain
        }
    });

    if (serviceDomain) throw new ApplicationException(ApplicationErrorCode.ALREADY_EXIST, "이미 해당 도메인은 사용중입니다.");

    const serviceName = await Service.findOne({
        where: {
            name: name
        }
    });

    if (serviceName) throw new ApplicationException(ApplicationErrorCode.ALREADY_EXIST, "이미 해당 이름은 사용중입니다.");
}

const serviceToJson = (service) => {
    return {
        id: Number(service.id), name: String(service.name), domain: String(service.domain), index: String(service.index)
    }
}