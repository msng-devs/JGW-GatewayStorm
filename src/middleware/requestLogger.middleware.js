const requestLogger = (req, res, next) => {

    const now = new Date().toISOString();
    const ip = req.ip;
    const url = req.url;
    const method = req.method;
    console.log(`[${now}] ${method} request to ${url} from ${ip}`);

    next();
}

module.exports = {requestLogger};