const { checkSchema } = require('express-validator')
const { apiRouteUpdateRequest , apiRouteAddRequest } = require( "../schema/apiRoute.schema");

const express = require("express");
const router = express.Router();

router.post("/:serviceId/apiRoute",checkSchema(apiRouteAddRequest), require("../controllers/apiRoute.contoller").createApiRoute);
router.put("/:serviceId/apiRoute/:id",checkSchema(apiRouteUpdateRequest), require("../controllers/apiRoute.contoller").updateApiRoute);
router.delete("/:serviceId/apiRoute/:id", require("../controllers/apiRoute.contoller").deleteApiRoute);
router.get("/:serviceId/apiRoute/:id", require("../controllers/apiRoute.contoller").findApiRouteById);
router.get("/:serviceId/apiRoute/", require("../controllers/apiRoute.contoller").findApiRouteByServiceId);


module.exports = router;