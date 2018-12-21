var callRestService = (function() {
	/**
	 * 每页记录数，默认20
	 */
	var PAGE_SIZE = 20;
	/**
	 * 默认超时时间
	 */
	var TIMEOUT = 60000;
	
	this.post = function(url, model, successCallback, errorCallback, isAsync) {
		$.ajax({
			type : 'POST',
			url : url,
			data : JSON.stringify(model), // '{"name":"' + model.name + '"}',  
			dataType : 'json',
			processData : false,
			async : isAsync !== false, // 是否异步传输，不传递该参数默认为true
			contentType : 'application/json',
			success : function(retData, textStatus){
				successHandler(successCallback, retData, textStatus);
			},
			error : function(XMLHttpRequest, textStatus, ex) {
				errorHandler(errorCallback, XMLHttpRequest, textStatus, ex);
			},
			timeout : TIMEOUT
		});
	};

	this.put = function(url, model, successCallback, errorCallback, isAsync) {
		$.ajax({
			type : 'PUT',
			url : url,
			data : JSON.stringify(model), // '{"name":"' + model.name + '"}',  
			dataType : 'json',
			processData : false,
			async : isAsync !== false,
			contentType : 'application/json',
			success : function(retData, textStatus){
				successHandler(successCallback, retData, textStatus);
			},
			error : function(XMLHttpRequest, textStatus, ex) {
				errorHandler(errorCallback, XMLHttpRequest, textStatus, ex);
			},
			timeout : TIMEOUT
		});
	};

	this.find = function(url, id, successCallback, errorCallback, isAsync) {
		$.ajax({
			type : 'GET',
			url : url + '/' + id,
			async : isAsync !== false,
			contentType : 'application/json',
			success : function(retData, textStatus){
				successHandler(successCallback, retData, textStatus);
			},
			error : function(XMLHttpRequest, textStatus, ex) {
				errorHandler(errorCallback, XMLHttpRequest, textStatus, ex);
			},
			timeout : TIMEOUT
		});
	};

	/**
	 * 根据给定资源url查询，一般用于有级联关系的查询，非根据资源主键进行查询,形如 http://ip:port/rest/cars/1/drivers
	 * @param url 请求url
	 * @param onSuccess 请求成功的处理
	 * @param onError 请求失败的处理
	 */
	this.findBy = function(url, successCallback, errorCallback, page, pageSize, async) {
		pageSize = pageSize || PAGE_SIZE;
		url = page ? url + "?page=" + page + "&pageSize=" + pageSize : url;
		$.ajax({
			type : 'GET',
			url : url,
			async : async,
			contentType : 'application/json',
			dataType : "json",
			success : successCallback,
			error : function(XMLHttpRequest, textStatus, ex) {
				errorHandler(errorCallback, XMLHttpRequest, textStatus, ex);
			},
			timeout : TIMEOUT
		});
	};
	
	/**
	 * 根据条件查询所有资源，不过这个方法是用post传递的查询
	 * @param url 请求url
	 * @param model 请求参数
	 * @param onSuccess 请求成功的处理
	 * @param onError 请求失败的处理
	 * @param page 分页参数，取第几页
	 * @param pageSize 分页参数，每页多少条记录，默认20条
	 */
	this.postFindBy = function(url, model, successCallback, errorCallback, page, pageSize, async) {
		pageSize = pageSize || PAGE_SIZE;
		url = page ? url + "?page=" + page + "&pageSize=" + pageSize : url;
		$.ajax({
			type : 'POST',
			url : url,
			async : async,
			data : JSON.stringify(model), // '{"name":"' + model.name + '"}',
			contentType : 'application/json',
			dataType : "json",
			success : successCallback,
			error : function(XMLHttpRequest, textStatus, ex) {
				errorHandler(errorCallback, XMLHttpRequest, textStatus, ex);
			},
			timeout : TIMEOUT
		});
	};
	this.findAll = function(url, successCallback, errorCallback, isAsync) {
		$.ajax({
			type : 'GET',
			url : url,
			dataType: "json",
			async : isAsync !== false,
			contentType : 'application/json',
			success : function(retData, textStatus){
				successHandler(successCallback, retData, textStatus);
			},
			error : function(XMLHttpRequest, textStatus, ex) {
				errorHandler(errorCallback, XMLHttpRequest, textStatus, ex);
			},
			timeout : TIMEOUT
		});
	};

	this.remove = function(url, id, successCallback, errorCallback, isAsync) {
		$.ajax({
			type : 'DELETE',
			url : url + '/' + id,
			async : isAsync !== false,
			contentType : 'application/json',
			success : function(retData, textStatus){
				successHandler(successCallback, retData, textStatus);
			},
			error : function(XMLHttpRequest, textStatus, ex) {
				errorHandler(errorCallback, XMLHttpRequest, textStatus, ex);
			},
			timeout : TIMEOUT
		});
	};
	
	/**
	 * 统一调用成功处理
	 */
	this.successHandler = function(successCallback, retData, textStatus) {
		if(successCallback && (typeof successCallback === "function")) {
			successCallback(retData, textStatus);
		}
	};
	
	/**
	 * 统一调用失败 异常处理
	 * 方便调用者，不需要手工弹出异常信息
	 */
	this.errorHandler = function(errorCallback, XMLHttpRequest, textStatus, ex) {
		if(errorCallback && (typeof errorCallback === "function")) {
			errorCallback(XMLHttpRequest, textStatus, ex);
		}
		else {
			
			// 如果调用者没有传递异常处理函数 ,则默认弹出异常信息
			var tips = JSON.parse(XMLHttpRequest.responseText);
			var errorCode = tips.code;
			var errorMsg = tips.message;
			
			// 业务异常信息
			// if (errorCode && (errorCode.toUpperCase().indexOf("DRM-") === 0)) {
			// 	new ZTEsoftDialog().alarm(errorMsg);
			// }
			// else {
			// 	// 其他异常信息
			// 	new ZTEsoftDialog().showException(errorMsg);
			// }
		}
	};
	
	return {
		post : post,
		put : put,
		find : find,
		findAll : findAll,
		findBy : findBy,
		postFindBy : postFindBy,
		remove : remove
	};
}());