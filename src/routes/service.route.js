const { checkSchema } = require('express-validator')
const {serviceAddRequest, serviceUpdateRequest} = require('../schema/service.schema')

const express = require("express");
const router = express.Router();

router.get("/", require("../controllers/service.contoller").getServices);
router.get("/:id", require("../controllers/service.contoller").findServiceById);
router.post("/", checkSchema(serviceAddRequest) ,require("../controllers/service.contoller").createService);
router.put("/:id",checkSchema(serviceUpdateRequest), require("../controllers/service.contoller").updateService);
router.delete("/:id", require("../controllers/service.contoller").deleteService);
module.exports = router;