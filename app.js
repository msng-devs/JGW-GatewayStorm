var express = require('express');
require('express-async-errors');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cors = require('cors');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public/dist')));
app.use(cors());
const{ requestLogger }= require('./src/middleware/requestLogger.middleware')
app.use(requestLogger)



//set route
app.use('/api/v1/service', require('./src/routes/apiRoute.route'));
app.use('/api/v1/service', require('./src/routes/service.route'));
app.use('/api/v1/role', require('./src/routes/role.route'));
app.use('/api/v1/method', require('./src/routes/method.route'));
app.use('/api/v1/routeOption', require('./src/routes/routeOption.route'));
app.use('/api/v1/ping', require('./src/routes/ping.route'));

//middleware
const {exceptionHandler} = require('./src/middleware/exceptionHandler.middleware');
const {processAuthentication} = require("./src/middleware/authentication.middleware");
app.use(exceptionHandler);


module.exports = app;



