exports.createPage = (req) => {
    const page = (req.query.page) ? req.query.page : 0;
    const limit = (req.query.size) ? req.query.size : 20;
    const offset = page * limit;

    return {page, limit, offset};
}