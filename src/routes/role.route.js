const express = require("express");
const router = express.Router();

router.get("/", require("../controllers/role.contoller").getRoles);
module.exports = router;