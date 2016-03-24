angular.module('desafio.factories', [])
.factory('utilsFactory', function($http, $rootScope, globals){
	var foo = 123,
		utilsFactory = {};

		utilsFactory.checkEmpty = function(arr){
			if(arr.length === 0){
				return true;
			}
			return false;
		};
		utilsFactory.onSubmit = function(args){
			console.log(args);
		};
		utilsFactory.guid = function() {
		  function s4() {
		    return Math.floor((1 + Math.random()) * 0x10000)
		      .toString(16)
		      .substring(1);
		  }
		  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
		    s4() + '-' + s4() + s4() + s4();
		};
		utilsFactory.formatUrlPath = function(path){
			var urlPath = globals.apiPath + 
						  path            + 
						  globals.pathFormat.json;
			return urlPath;
		};
		utilsFactory.getAveragePrice = function(product){
			if(product === undefined){
				return 0;
			}
			var avgObj = shareData['/products'].reduce(function(memo, curr){
				if(product.name == curr.name && product.id != curr.id){ //same product but not himself
					memo.count++;
					memo.total+= curr.price;
				}
				return memo
			}, {
				count: 0,
				total: 0
			});
			return ((avgObj.total + product.price) / (avgObj.count + 1)); 
		};
		utilsFactory.hashStringToColor = function(str) {
			if(str === undefined){
				return;
			}
			var djb2 = function(str){
			  var hash = 5381;
			  for (var i = 0; i < str.length; i++) {
			    hash = ((hash << 5) + hash) + str.charCodeAt(i); /* hash * 33 + c */
			  }
			  return hash;
			}
			var hash = djb2(str);
			var r = (hash & 0xFF0000) >> 16;
			var g = (hash & 0x00FF00) >> 8;
			var b = hash & 0x0000FF;
			return "#" + ("0" + r.toString(16)).substr(-2) + ("0" + g.toString(16)).substr(-2) + ("0" + b.toString(16)).substr(-2);
		};
		utilsFactory.formatMessage = function(responseMessage){
			var message = '';
        	for(i in responseMessage){
        		message += i + ' - ' + responseMessage[i] + '\n';
        	}
        	return message;
		};

	return utilsFactory;
})