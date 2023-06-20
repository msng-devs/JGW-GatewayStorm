const serviceAddRequest = {
    name: {
        notEmpty: true,
        in: ['body'],
        isLength: {
            errorMessage: 'name 는 1~45 자 이여야 합니다.',
            options: { min: 1 ,max: 45}
        }
    },
    index: {
        notEmpty: false,
        in: ['body'],
        isLength: {
            errorMessage: 'index는 최대 256자 입니다.',
            options: { max: 256}
        }
    },

    domain: {
        notEmpty: true,
        in: ['body'],
        isLength: {
            errorMessage: 'domain 는 최대 200자 입니다.',
            options: { min: 1 ,max: 200}
        }
    },
}

const serviceUpdateRequest = {
    name: {
        notEmpty: true,
        in: ['body'],
        isLength: {
            errorMessage: 'name 는 1~45 자 이여야 합니다.',
            options: { min: 1 ,max: 45}
        }
    },
    index: {
        notEmpty: false,
        in: ['body'],
        isLength: {
            errorMessage: 'index는 최대 256자 입니다.',
            options: { max: 256}
        }
    },

    domain: {
        notEmpty: true,
        in: ['body'],
        isLength: {
            errorMessage: 'domain 는 최대 200자 입니다.',
            options: { min: 1 ,max: 200}
        }
    },
}

module.exports = {
    serviceAddRequest,
    serviceUpdateRequest
}