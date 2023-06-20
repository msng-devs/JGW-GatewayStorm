const express = require("express");
const router = express.Router();

router.get("/",require("../controllers/method.contoller").getMethods);
module.exports = router;