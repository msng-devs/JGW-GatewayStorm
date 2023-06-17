const admin = require("firebase-admin");
require('dotenv').config({ path: `.env.${process.env.NODE_ENV}` });

admin.initializeApp({
    credential: admin.credential.cert('firebase.json'),
});
console.log("firebase admin initialized");
module.exports.admin = admin;