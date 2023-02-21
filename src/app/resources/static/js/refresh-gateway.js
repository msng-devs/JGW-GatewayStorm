
const JsLoadingOverlay = window.JsLoadingOverlay
var configs = {
    'overlayBackgroundColor': '#333333',
    'overlayOpacity': 0.6,
    'spinnerIcon': 'ball-fall',
    'spinnerColor': '#00bc8c',
    'spinnerSize': '1x',
    'overlayIDName': 'overlay',
    'spinnerIDName': 'spinner',
    'offsetY': 0,
    'offsetX': 0,
    'lockScroll': true,
    'containerID': null,
};
var csrf_token  = $("meta[name=_csrf]").attr("content");
var main = {
    init : function () {
        var _this = this;
        $('#btn-gateway-refresh').on('click', function () {
            if($("input:checkbox[id='refresh-agree']").is(":checked") === true){
                JsLoadingOverlay.show(configs);
                _this.firebase_login();
            }

        });

    },

    firebase_login : function () {
        var data = {
            email : $("#refresh-id").val(),
            password : $("#refresh-pw").val(),
            returnSecureToken: true
        };
        $.ajax({
            type: 'POST',
            url: "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key="+$("meta[name=firebase-key]").attr("content"),
            contentType:'application/json',
            data: JSON.stringify(data)
        }).done(function(data) {
            var token = data.idToken
            get_accessToken(token)
        }).fail(function (error) {
            console.log(error)
            JsLoadingOverlay.hide();
            alert("email이나 비밀번호가 잘못되었습니다.");

        });
    }
};
main.init();

function gateway_refresh (accessToken){
        $.ajax({
            type: 'POST',
            xhrFields: {
               withCredentials: true
            },
            url: "https://api.hrabit64.xyz/refresh",
            dataType: 'json',
            headers : {"Authorization" : "bearer " +accessToken},
            crossDomain: true,
            contentType:'application/json; charset=utf-8'
        }).done(function(data) {
            clean_accessToken(accessToken)

        }).fail(function (error) {
            JsLoadingOverlay.hide();
            alert(JSON.stringify(error));

        });
    }
function get_accessToken(idtoken){
        $.ajax({
            type: 'POST',
            xhrFields: {
               withCredentials: true
            },
            url: "https://api.hrabit64.xyz/auth/api/v2/auth/authorization?idToken="+idtoken,
            dataType: 'json',
            crossDomain: true,
            contentType:'application/json; charset=utf-8'
        }).done(function(data) {
            gateway_refresh(data.access_token)
        }).fail(function (error) {
            JsLoadingOverlay.hide();
            alert(JSON.stringify(error));
        });
    }
    function clean_accessToken(accessToken){
        $.ajax({
            type: 'DELETE',
            xhrFields: {
               withCredentials: true
            },
            url: "https://api.hrabit64.xyz/auth/api/v2/auth/revoke?accessToken="+accessToken,
            dataType: 'json',
            crossDomain: true,
            contentType:'application/json; charset=utf-8'
        }).done(function(data) {
            JsLoadingOverlay.hide();
            alert("성공!");
        }).fail(function (error) {
            JsLoadingOverlay.hide();
            alert(JSON.stringify(error));
        });
    }

