const { checkSchema, validationResult } = require("express-validator");
const ApplicationException = require("../utlis/exception/application.exception");
const ApplicationErrorCode = require("../utlis/exception/application.exception");

const requestBodyValidate = (schema) => {
    return [
        checkSchema(schema),
        (req, res, next) => {
            const errors = validationResult(req);
            if (!errors.isEmpty()) {
                throw ApplicationException(ApplicationErrorCode.REQUEST_ARGS_ERROR, errors.array());
            }
            next();
        },
    ];
};

module.exports = requestBodyValidate;