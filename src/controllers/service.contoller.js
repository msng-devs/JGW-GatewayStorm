const Service = require('../models/service.model');
const {createPage} = require("../utlis/pagenation");
const {ApplicationException, ApplicationErrorCode} = require("../utlis/exception/application.exception");

exports.getServices = async (req, res, next) => {

    const services = await Service.findAll({
        order: [['id', 'DESC']]
    });
    res.json(services.map(serviceToJson));
};

exports.createService = async (req, res, next) => {

    await checkUniqueName(req.body.name);
    await checkUniqueDomain(req.body.domain);
    checkDomain(req.body.domain);
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

    if(service.name !== req.body.name) await checkUniqueName(req.body.name);
    if(service.domain !== req.body.domain) await checkUniqueDomain(req.body.domain);

    checkDomain(req.body.domain);
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

const checkUniqueDomain = async (domain) => {
    const serviceDomain = await Service.findOne({
        where: {
            domain: domain
        }
    });

    if (serviceDomain) throw new ApplicationException(ApplicationErrorCode.ALREADY_EXIST, "이미 해당 도메인은 사용중입니다.");
}
const checkUniqueName = async (name) => {

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

const checkDomain = (domain) => {
    const urlRegex = /(http[s]?:\/\/)?([^\s(["<,>]*\.[^\s[",><]+|localhost)(:\d+)?(\/[^\s]*)?/g;

    if(!urlRegex.test(domain)) throw new ApplicationException(ApplicationErrorCode.REQUEST_ARGS_ERROR, "도메인 형식이 올바르지 않습니다.")
}