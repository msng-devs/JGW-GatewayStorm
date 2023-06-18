const role = require("../models/role.model");

exports.getRoles = async (req, res, next) => {
    try {
        const roles = await role.findAll();
        res.json(roles);
    } catch (error) {
        next(error);
    }
}