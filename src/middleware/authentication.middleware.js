const {admin} = require("../../config/firebase.config");
const Member = require('../models/member.model');
const {ApplicationException,ApplicationErrorCode} = require("../utlis/exception/application.exception");

const processAuthentication = async (req, res, next) => {

    const idToken = req.headers.authorization;
    if(idToken === undefined){
        throw new ApplicationException(ApplicationErrorCode.AUTH_FAILED, "인증에 실패했습니다. 토큰이 존재하지 않습니다.");
    }
    const decodedToken = await verifyToken(idToken)
    await checkMemberInfo(decodedToken);

    next();
};

const checkMemberInfo = async (decodedToken) => {
    const member = await Member.findByPk(decodedToken.uid)
    if(!member) throw new ApplicationException(ApplicationErrorCode.AUTH_FAILED, "인증에 실패했습니다. 회원정보가 존재하지 않습니다.");
    if(member.role < 5) throw new ApplicationException(ApplicationErrorCode.AUTH_FAILED, "인증에 실패했습니다. 권한이 없습니다.");
}
const verifyToken = async (idToken) => {
    const decodedToken = await admin.auth().verifyIdToken(idToken);
    if (decodedToken) {
        return decodedToken;
    } else {
        throw new ApplicationException(ApplicationErrorCode.AUTH_FAILED, "인증에 실패했습니다. 올바르지 않은 토큰입니다.");
    }
};

module.exports = {
    processAuthentication
}