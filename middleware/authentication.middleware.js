const {admin} = require("../config/firebase.config");
const Member = require('../models/member.model');
const ApplicationException = require("../utlis/exception/application.exception");
const ApplicationErrorCode = require("../utlis/exception/application.exception");


exports.processAuthentication = async (req, res, next) => {
    const idToken = req.headers.authorization;
    if(idToken === undefined){
        throw ApplicationException(ApplicationErrorCode.AUTH_FAILED, "인증에 실패했습니다. 토큰이 존재하지 않습니다.");
    }
    verifyToken(idToken)
        .then((decodedToken) => {
            Member.findByPk(decodedToken.uid)
                .then((member) => {
                    if (member) {
                        checkMemberInfo(member);
                        req.member = member.name;
                        req.uid = member.id;
                        next();
                    } else {
                        throw ApplicationException(ApplicationErrorCode.AUTH_FAILED, "인증에 실패했습니다. 회원정보가 존재하지 않습니다.");
                    }
                })
                .catch((err) => {
                    throw ApplicationException(ApplicationErrorCode.AUTH_FAILED, "인증에 실패했습니다. 회원정보를 불러오는데 실패했습니다.");
                });
        })
};

const checkMemberInfo = (member) => {
    if(member.role < 5) throw ApplicationException(ApplicationErrorCode.AUTH_FAILED, "인증에 실패했습니다. 권한이 없습니다.");
}

const verifyToken = async (idToken) => {
    const decodedToken = await admin.auth().verifyIdToken(idToken);
    if (decodedToken) {
        return decodedToken;
    } else {
        throw ApplicationException(ApplicationErrorCode.AUTH_FAILED, "인증에 실패했습니다. 올바르지 않은 토큰입니다.");
    }
};