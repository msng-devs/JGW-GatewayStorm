const { checkSchema } = require('express-validator')
const { apiRouteUpdateRequest , apiRouteAddRequest } = require( "../schema/apiRoute.schema");

const express = require("express");
const router = express.Router();

router.post("/",checkSchema(apiRouteAddRequest), require("../controllers/apiRoute.contoller").createApiRoute);
router.put("/:id",checkSchema(apiRouteUpdateRequest), require("../controllers/apiRoute.contoller").updateApiRoute);
router.delete("/:id", require("../controllers/apiRoute.contoller").deleteApiRoute);
router.get("/:id", require("../controllers/apiRoute.contoller").findApiRouteById);
router.get("/", require("../controllers/apiRoute.contoller").findApiRouteByServiceId);


module.exports = router;