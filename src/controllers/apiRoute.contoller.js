const ApiRoute = require('../models/apiRoute.model');
const Method = require('../models/method.model');
const Service = require('../models/service.model');
const Role = require('../models/role.model');
const RouteOption = require('../models/routeOption.model');

const {ApplicationException, ApplicationErrorCode} = require("../utlis/exception/application.exception");
const {createPage} = require("../utlis/pagenation");

exports.getApiRoute = async (req, res, next) => {
    const apiRoute = await ApiRoute.findByPk(req.params.id);
    if (!apiRoute) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "Api Route not found");
    res.json(apiRouteToJson(apiRoute));
};

exports.createApiRoute = async (req, res, next) => {
    const foreignItems = await checkExistForeignTable(req.body.method, req.body.role_id, null, req.body.option_id)
    await checkUnique(req.body.path, foreignItems.method.id, req.params.serviceId)

    const apiRoute = {
        path: req.body.path,
        method: req.body.method,
        role: (req.body.role_id) ? req.body.role_id : null,
        service: req.params.serviceId,
        routeOption: req.body.option_id
    };

    const newApiRoute = await ApiRoute.create(apiRoute);
    console.log(newApiRoute)

    res.json(apiRouteToJson(newApiRoute));

}

exports.findApiRouteById = async (req, res, next) => {

    const apiRoute = await ApiRoute.findByPk(req.params.id);
    if (!apiRoute) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "Api Route not found");
    res.json(apiRouteToJson(apiRoute));
}

exports.findApiRouteByServiceId = async (req, res, next) => {
    const page = createPage(req);
    const apiRoute = await ApiRoute.findAll({
        where: {
            service: req.params.serviceId,

        },
        offset: page.offset,
        limit: page.limit,
        order: [['path', 'ASC'], ['id', 'DESC']]
    });

    res.json(apiRoute.map(apiRouteToJson));
}

exports.updateApiRoute = async (req, res, next) => {

    const apiRoute = await ApiRoute.findByPk(req.params.id);
    console.log(apiRoute)
    if (!apiRoute) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "해당 라우트를 찾을 수 없습니다.");
    const foreignItems = await checkExistForeignTable(req.body.method, req.body.role_id, null, req.body.option_id)
    await checkUnique(req.body.path, req.body.method, apiRoute.service)

    await apiRoute.update({
        path: req.body.path,
        method: req.body.method,
        role: req.body.role_id,
        routeOption: req.body.option_id
    });
    res.json(apiRouteToJson(apiRoute));
}

exports.deleteApiRoute = async (req, res, next) => {

    const apiRoute = await ApiRoute.findByPk(req.params.id);
    if (!apiRoute) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "해당 라우트를 찾을 수 없습니다.");
    await apiRoute.destroy();
    res.status(204).end();

}

const checkUnique = async (path, method, service) => {
    const apiRoute = await ApiRoute.findOne({
        where: {
            path: path,
            method: method,
            service: service
        }
    });
    if (apiRoute) throw new ApplicationException(ApplicationErrorCode.ALREADY_EXISTS, "이미 해당 서비스내에 같은 메소드와 같은 path를 지닌 route 정보가 있습니다.");
}

const checkExistForeignTable = async (methodId, roleId, serviceId, routeOptionId) => {

    let method = null;
    let role = null;
    let service = null;
    let routeOption = null;

    if (methodId) {
        method = await Method.findByPk(methodId);
        if (!method) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "해당 Method를 찾을 수 없습니다.");
    }
    if (roleId) {
        role = await Role.findByPk(roleId);
        if (!role) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "해당 Role을 찾을 수 없습니다.");
    }
    if (serviceId) {
        service = await Service.findByPk(serviceId);
        if (!service) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "해당 Service를 찾을 수 없습니다.");
    }
    if (routeOptionId) {
        routeOption = await RouteOption.findByPk(routeOptionId);
        if (!routeOption) throw new ApplicationException(ApplicationErrorCode.NOT_FOUND, "해당 RouteOption을 찾을 수 없습니다.");
    }
    return {
        method: method,
        role: role,
        service: service,
        routeOption: routeOption
    }
}

const apiRouteToJson = (apiRoute) => {
    return {
        id: Number(apiRoute.id),
        path: String(apiRoute.path),
        role_id: (apiRoute.role === null) ? null : Number(apiRoute.role),
        method_id: Number(apiRoute.method),
        service_id: Number(apiRoute.service),
        route_option_id: Number(apiRoute.routeOption),
    }
}