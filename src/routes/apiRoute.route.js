const { checkSchema } = require('express-validator')
const { apiRouteUpdateRequest , apiRouteAddRequest } = require( "../schema/apiRoute.schema");
const{ processAuthentication }= require('../middleware/authentication.middleware');

const express = require("express");
const router = express.Router();

router.post("/:serviceId/apiRoute",[processAuthentication,checkSchema(apiRouteAddRequest)], require("../controllers/apiRoute.contoller").createApiRoute);
router.put("/:serviceId/apiRoute/:id",[processAuthentication,checkSchema(apiRouteUpdateRequest)], require("../controllers/apiRoute.contoller").updateApiRoute);
router.delete("/:serviceId/apiRoute/:id", processAuthentication ,require("../controllers/apiRoute.contoller").deleteApiRoute);
router.get("/:serviceId/apiRoute/:id",processAuthentication ,require("../controllers/apiRoute.contoller").findApiRouteById);
router.get("/:serviceId/apiRoute/",processAuthentication ,require("../controllers/apiRoute.contoller").findApiRouteByServiceId);


module.exports = router;