var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const{ processAuthentication }= require('./middleware/authentication.middleware');
const{ exceptionHandler }= require('./middleware/exceptionHandler.middleware');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public/dist')));

//middleware
app.use(processAuthentication)
app.use(exceptionHandler)

module.exports = app;
