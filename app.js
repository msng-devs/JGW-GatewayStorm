var express = require('express');
require('express-async-errors');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');


var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public/dist')));

const env = process.env.NODE_ENV || 'local';
if(env !== 'test'){
    const{ processAuthentication }= require('./src/middleware/authentication.middleware');
    app.use(processAuthentication);
}




//set route
const apiRouter = require('./src/routes/apiRoute.route');
app.use('/api/v1/apiRoute', apiRouter);

//middleware
const{ exceptionHandler }= require('./src/middleware/exceptionHandler.middleware');
const {processAuthentication} = require("./src/middleware/authentication.middleware");
app.use(exceptionHandler);


module.exports = app;



