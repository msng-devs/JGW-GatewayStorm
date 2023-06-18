exports.createPage = (req) => {
    const page = req.query.page;
    const limit = req.query.size;
    const offset = (page - 1) * limit;
    return {page, limit, offset};
}