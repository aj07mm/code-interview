angular.module('microapps.services', ['microapps.factories'])
.service('REST', ['$http', 'globals', 'utilsFactory', function($http, globals, utilsFactory){
	this.get = function(path, resourceId, callback){
		var urlPath = utilsFactory.formatUrlPath(path + '/' + resourceId);
		//if is already here use, else $http.get
		$http.get(urlPath, {}).success(function(data) {
          // prepare data here
          callback(data);
        });
	};
	
}])
.service('doTransaction', ['$http', 'globals', 'REST', 'utilsFactory', function($http, globals, REST, utilsFactory){
  this.checkout = function(data, callback){
    var req = {
      method: 'POST',
      url: 'http://localhost:3000/checkout',
      data: JSON.stringify({
        "authentication" : {
          "userId" : "8a8294174b7ecb28014b9699220015cc",
          "password" : "sy6KJsT8",
          "entityId" : "8a8294174b7ecb28014b9699220015ca"
        },
        "amount" : data['amount'],
        "currency" : data['currency'],
        "paymentType" : data['paymentType']
      })
    };
    $http(req).then(function(response) {
      // swal("Sent!", '', "success")
      // prepare data here
      if(callback !== undefined){
        callback(response);
      }
    }, function(response){
      // swal("Bad!", '', "error")
    })
  };
  this.pay = function(data, callback){
  };
}]);

