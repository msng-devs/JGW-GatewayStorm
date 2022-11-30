var main = {
    init : function () {
        var _this = this;
        $('#btn-service-update').on('click', function () {
            _this.service_update();
        });
        $('#btn-service-add').on('click', function () {
            _this.service_add();
        });
        $('#btn-service-check-rm').on('click', function () {
            _this.service_rm_check();
        });
        $('#btn-service-rm').on('click', function () {
            _this.service_rm();
        });
        $('#edit-category-id').on('change', function () {
            _this.category_index_change();
        });
        $('#btn-category-edit').on('click', function () {
            _this.category_edit();
        });
        $('#btn-category-remove').on('click', function () {
            _this.category_remove();
        });
    },
    service_update : function () {
        var data = {
            name : $("#update-service-name").val(),
            index : $("#update-service-index").val(),
            domain : $("#update-service-domain").val(),
        };

        $.ajax({
            type: 'PUT',
            url: "/api/v1/service/" + $("#update-service-id").text(),
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function() {
            alert('서비스 정보가 업데이트 되었습니다!');
            window.location.href = '/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },
    service_add : function () {
        var data = {
            name : $("#add-service-name").val(),
            index : $("#add-service-index").val(),
            domain : $("#add-service-domain").val()
        };

        $.ajax({
            type: 'POST',
            url: "/api/v1/service/",
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function() {
            alert('성공적으로 서비스가 추가되었습니다.');
            window.location.href = '/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },

    path_add : function () {
        var data = {
            category_id: $('#category').val(),
            content: simplemde.value(),
            title: $('#title').val()
        };

        $.ajax({
            type: 'POST',
            url: "/api/v1/posts",
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function() {
            alert('글이 등록되었습니다.');
            window.location.href = '/posts/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },
    path_update : function () {
        var data = {
            service_name : $("#update-service-name").val(),
            service_index : $("#update-service-index").val(),
            service_domain : $("#update-service-domain").val(),
        };

        $.ajax({
            type: 'POST',
            url: "/api/v1/posts",
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function() {
            alert('글이 등록되었습니다.');
            window.location.href = '/posts/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },
    service_rm_check: function (){
        $('#update-service').modal('hide');
        $('#delete-service').modal('show');
        $("#rm-service-id").text($("#update-service-id").text());
        $("#rm-service-index").text($("#update-service-name").text() + " 해당 서비스를 삭제하면, 하위 path도 모두 함께 삭제되며, 다시는 복구할 수 없습니다. 진행하시겠습니까?");

        },
    service_rm : function () {

        $.ajax({
            type: 'DELETE',
            url: "/api/v1/service/" + $("#rm-service-id").text(),
            dataType: 'json',
            contentType:'application/json; charset=utf-8'
        }).done(function() {
            alert('성공적으로 삭제되었습니다.');
            window.location.href = '/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    },
    path_rm : function () {
        var data = {
            category_id: $('#category').val(),
            content: simplemde.value(),
            title: $('#title').val()
        };

        $.ajax({
            type: 'POST',
            url: "/api/v1/posts",
            dataType: 'json',
            contentType:'application/json; charset=utf-8',
            data: JSON.stringify(data)
        }).done(function() {
            alert('글이 등록되었습니다.');
            window.location.href = '/posts/';
        }).fail(function (error) {
            alert(JSON.stringify(error));
        });
    }

};

main.init();

    jQuery('#add-path-option').change(function() {
	var state = jQuery('#option').val();
	if ( state === 'RBAC' ) {
		jQuery('#add-path-role').show();
        jQuery('#add-path-role-label').show();
	} else {
		jQuery('#add-path-role').hide();
        jQuery('#add-path-role-label').hide();
	}
    });
function service_update_modal(tr_id){

    var td = $('#'+tr_id).closest('tr').children();

    var service_name = td.eq(0).text()
    var service_index = td.eq(1).text()
    var service_domain = td.eq(2).text()
    console.log(service_name,service_index,service_domain)
    $('#update-service').modal('show');
    $("#update-service-id").text(tr_id);
    $("#update-service-name").val(service_name)
    $("#update-service-index").val(service_index)
    $("#update-service-domain").val(service_domain)

}
