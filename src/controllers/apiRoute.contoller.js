const ApiRoute = require('../models/apiRoute.model');
const Method = require('../models/method.model');
const Service = require('../models/service.model');
const Role = require('../models/role.model');
const RouteOption = require('../models/routeOption.model');

const {ApplicationException,ApplicationErrorCode} = require("../utlis/exception/application.exception");

exports.getApiRoute = async (req, res, next) => {
    const apiRoute = await ApiRoute.findByPk(req.params.id);
    if(!apiRoute) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND,"Api Route not found");
    res.json(apiRoute);
};

exports.createApiRoute = async (req, res, next) => {
    const foreignItems = await checkExistForeignTable(req.body.method,req.body.role_id,req.body.service_Id,req.body.option)
    await checkUnique(req.body.path,req.body.method,req.body.serviceId)

    const apiRoute = new ApiRoute({
        path: req.body.path,
        method: foreignItems.method,
        role: foreignItems.role,
        service: foreignItems.service,
        routeOption: foreignItems.routeOption
    });
    const newApiRoute = await ApiRoute.create(req.body);
    res.json(newApiRoute);

}

exports.findApiRouteById = async (req, res, next) => {

    const apiRoute = await ApiRoute.findByPk(req.params.id);
    if (!apiRoute) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND,"Api Route not found");
    res.json(apiRoute);
}

exports.findApiRouteByServiceId = async (req, res, next) => {
    const apiRoute = await ApiRoute.findAll({
        where: {
                serviceId: req.query.serviceId
        }
    });
    res.json(apiRoute);
}

exports.updateApiRoute = async (req, res, next) => {

    const apiRoute = await ApiRoute.findByPk(req.params.id);
    if(!apiRoute) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND,"Api Route not found");

    await checkUnique(req.body.path,req.body.method,apiRoute.service.id)

    await apiRoute.update(req.body);
    res.json(apiRoute);
}

exports.deleteApiRoute = async (req, res, next) => {

    const apiRoute = await ApiRoute.findByPk(req.params.id);
    if(!apiRoute) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND,"Api Route not found");
    await apiRoute.destroy();
    res.status(204).end();

}


const checkUnique = async (path,method,service) => {
    const apiRoute = await ApiRoute.findOne({
        where: {
            path: path,
            method: method,
            serviceId: service
        }
    });
    if(apiRoute) throw new ApplicationException(ApplicationErrorCode.ALREADY_EXISTS,"이미 해당 서비스내에 같은 메소드와 같은 path를 지닌 route 정보가 있습니다.");
}

const checkExistForeignTable = async (methodId,roleId,serviceId,routeOptionId) => {

    let method = null;
    let role = null;
    let service = null;
    let routeOption = null;

    if(methodId){
        method = await Method.findByPk(methodId);
        if(!method) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND,"해당 Method를 찾을 수 없습니다.");
    }
    if(roleId){
        role = await Role.findByPk(roleId);
        if(!role) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND,"해당 Role을 찾을 수 없습니다.");
    }
    if(serviceId){
        service = await Service.findByPk(serviceId);
        if(!service) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND,"해당 Service를 찾을 수 없습니다.");
    }
    if(routeOptionId){
        routeOption = await RouteOption.findByPk(routeOptionId);
        if(!routeOption) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND,"해당 RouteOption을 찾을 수 없습니다.");
    }
    return {
        method: method,
        role: role,
        service: service,
        routeOption: routeOption
    }
}