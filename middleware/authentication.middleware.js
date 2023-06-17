const {admin} = require("../config/firebase.config");

exports.verifyToken = async (req, res, next) => {
    const idToken = req.headers.authorization;

    try {
        const decodedToken = await admin.auth().verifyIdToken(idToken);
        if (decodedToken) {
            req.body.uid = decodedToken.uid;
            return next();
        } else {
            return res.status(401).send('You are not authorized to make this request');
        }
    } catch (e) {
        return res.status(401).send('You are not authorized to make this request');
    }
};
