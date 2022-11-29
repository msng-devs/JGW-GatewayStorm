var main = {
    init : function () {
        var _this = this;
        $('#btn-save').on('click', function () {
            _this.save();
        });
        $('#btn-category-add').on('click', function () {
            _this.category_add();
        });
        $('#btn-edit').on('click', function () {
            _this.update();
        });
        $('#btn-remove').on('click', function () {
            _this.remove();
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
function service_update_modal(tr_name){
    var td = $('#'+tr_name).closest('tr').children();

    var service_name = tr_name
    var service_index = td.eq(1).text()
    var service_domain = td.eq(2).text()

    $("#update-service-name").text(service_name)
    $("#update-service-index").text(service_index)
    $("#update-service-domain").text(service_domain)
    $('#update-service').modal('show');
}
