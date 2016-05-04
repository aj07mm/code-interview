angular.module('microapps.controllers', ['microapps.factories', 'microapps.services'])
.controller('checkoutCtrl', ['$scope', '$http', '$rootScope', 'globals', 'doTransaction', 'utilsFactory', 
	function($scope, $http, $rootScope, globals, doTransaction, utilsFactory) {

		$scope.brands = globals.payment.brands;
		$scope.types = globals.payment.types;
		$scope.currencies = globals.payment.currencies;
		$scope.transaction = {};

		utilsFactory.setState('checkout');
		$scope.getState = utilsFactory.getState

		$scope.send = function(transaction){
			$scope.state = {
				checkout : false,
				payment : true
			};
			doTransaction.checkout(transaction, function(response){
				utilsFactory.setState('payment');
				console.log(utilsFactory.state)
				console.log(response)
			})
		};
	}
])
.controller('paymentCtrl', ['$scope', '$http', '$rootScope', 'globals', 'doTransaction', 'utilsFactory', 
	function($scope, $http, $rootScope, globals, doTransaction, utilsFactory) {

		$scope.getState = utilsFactory.getState

		$scope.send = function(transaction){
			doTransaction.pay(transaction, function(response){
				console.log(response)
			})
		};
	}
]);