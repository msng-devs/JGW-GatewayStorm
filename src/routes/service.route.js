const { checkSchema } = require('express-validator')
const {serviceAddRequest, serviceUpdateRequest} = require('../schema/service.schema')

const express = require("express");
const router = express.Router();
const{ processAuthentication }= require('../middleware/authentication.middleware');

router.get("/", processAuthentication ,require("../controllers/service.contoller").getServices);
router.get("/:id",processAuthentication , require("../controllers/service.contoller").findServiceById);
router.post("/",[processAuthentication ,checkSchema(serviceAddRequest)] ,require("../controllers/service.contoller").createService);
router.put("/:id",[processAuthentication ,checkSchema(serviceUpdateRequest)], require("../controllers/service.contoller").updateService);
router.delete("/:id",processAuthentication, require("../controllers/service.contoller").deleteService);
module.exports = router;