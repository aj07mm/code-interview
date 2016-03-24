angular.module('desafio.services', ['desafio.factories'])
.service('REST', function($http, $rootScope, globals, utilsFactory){
	this.get = function(path, resourceId, callback){
		var urlPath = utilsFactory.formatUrlPath(path + '/' + resourceId);
		//if is already here use, else $http.get
		$http.get(urlPath, {}).success(function(data) {
          // prepare data here
          callback(data);
        });
	};
	this.getAll = function(path, callback){
		var urlPath = utilsFactory.formatUrlPath(path);
        $http.get(urlPath, {}).success(function(data) {
          // prepare data here
          callback(data.results);
        });
	};
	this.post = function(path, postData, callback){
		var urlPath = utilsFactory.formatUrlPath(path);
        $http.post(urlPath, postData).then(function(response) {
          swal("Created!", '', "success")
          // prepare data here
          if(callback !== undefined){
            callback(response);
          }
        }, function(response){
        	var message = utilsFactory.formatMessage(response.data);
        	swal("Bad!", message, "error")
        })
	};
	this.put = function(path, resourceId, resource, callback){
		var urlPath = utilsFactory.formatUrlPath(path + '/' + resourceId);
		$http.put(urlPath, resource).then(function(response) {
          swal("Updated!", '', "success")
          // prepare data here
          callback(response);
        }, function(response){
        	var message = utilsFactory.formatMessage(response.data);
        	swal("Bad!", message, "error")
        })
	};
	this.delete = function(path, callback){
		var urlPath = utilsFactory.formatUrlPath(path);
        $http.delete(urlPath, {}).then(function(response) {
          swal("Deleted!", '', "success")
          // prepare data here
          callback(response);
        }, function(response){
        	var message = utilsFactory.formatMessage(response.data);
        	swal("Bad!", message, "error")
        })
	};
});