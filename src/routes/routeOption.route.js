const express = require("express");
const router = express.Router();

router.get("/",require("../controllers/routeOption.contoller").getRouteOptions);
module.exports = router;