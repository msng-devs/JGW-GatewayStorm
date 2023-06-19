const { Schema } = require('express-validator')

const apiRouteAddRequest = {
    path: {
        notEmpty: true,
        in: ['body'],
        isLength: {
            errorMessage: 'path 는 1~45 자 이여야 합니다.',
            options: { min: 1 ,max: 45}
        }
    },
    method: {
        notEmpty: true,
        in: ['body'],
        isInt: {
            errorMessage: 'method 는 양수여야 합니다.',
        }
    },
    role_id: {
        notEmpty: false,
        in: ['body'],
        isInt: {
            errorMessage: 'role id 는 양수여야 합니다.',
        }
    },
    service_id: {
        notEmpty: true,
        in: ['body'],
        isInt: {
            errorMessage: 'service id 는 양수여야 합니다.',
        }
    },
    option:{
        notEmpty: true,
        in: ['body'],
        isInt: {
            errorMessage: 'option 는 양수여야 합니다.',
        }
    }
}

const apiRouteUpdateRequest = {
    path: {
        notEmpty: true,
        in: ['body'],
        isLength: {
            errorMessage: 'path 는 1~45 자 이여야 합니다.',
            options: { min: 1 ,max: 45}
        }
    },
    method: {
        notEmpty: true,
        in: ['body'],
        isInt: {
            errorMessage: 'method 는 양수여야 합니다.',
        }
    },
    role_id: {
        notEmpty: false,
        in: ['body'],
        isInt: {
            errorMessage: 'method 는 양수여야 합니다.',
        }
    },
    option:{
        notEmpty: true,
        in: ['body'],
        isInt: {
            errorMessage: 'option 는 양수여야 합니다.',
        }
    }
}

module.exports = {
    apiRouteAddRequest,
    apiRouteUpdateRequest
}