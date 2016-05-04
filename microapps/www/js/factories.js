angular.module('microapps.factories', [])
.factory('utilsFactory', ['$http', '$rootScope', 'globals', function($http, $rootScope, globals){
	var utilsFactory = {};

	utilsFactory['state'] = {};

	utilsFactory.setState = function(state){
		utilsFactory.state = state;
	}
	utilsFactory.getState = function(){
		return utilsFactory.state;
	};

	utilsFactory.checkEmpty = function(arr){
		if(arr.length === 0){
			return true;
		}
		return false;
	};
	utilsFactory.formatUrlPath = function(path){
		var urlPath = globals.apiPath + 
					  path
		return urlPath;
	};
	utilsFactory.formatMessage = function(responseMessage){
		var message = '';
    	for(i in responseMessage){
    		message += i + ' - ' + responseMessage[i] + '\n';
    	}
    	return message;
	};
	utilsFactory.getOptions = function(path, data){
	  return {
	      port: 443,
	      host: 'test.oppwa.com',
	      path: path,
	      method: 'POST',
	      headers: {
	        'Content-Type': 'application/x-www-form-urlencoded',
	        'Content-Length': data.length
	      }
	  };
	}

	return utilsFactory;
}])