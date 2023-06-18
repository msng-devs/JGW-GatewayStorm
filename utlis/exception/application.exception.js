class ApplicationException extends Error {
    constructor(code,message) {
        super(message);
        this.name = "ApplicationException";
        this.code = code;
    }
}

const ApplicationErrorCode = {
    UNKNOWN_ERROR: {
        status: 500,
        code: "GS_000",
        title: "Unknown Error",
    },
    NOT_FOUND: {
        status: 404,
        code: "GS_001",
        title: "Not Found",
    },
    AUTH_FAILED:{
        status: 403,
        code: "GS_002",
        title: "Authentication Failed",
    }
}

module.exports = ApplicationException;
module.exports = ApplicationErrorCode;