angular.module('desafio.controllers', ['desafio.factories', 'desafio.services'])
.controller('productCtrl', function($scope, $state, REST, utilsFactory) {
	//dar um jeito nisso
	REST.getAll('/purchases', function(purchases){
		$scope.purchases = purchases;
	});
	REST.getAll('/products', function(products){
		$scope.products = products;
	});
	$scope.create = function(resource){
		REST.post('/products', resource, function(response){
			$state.go('products');
		});
	};
	$scope.update = function(resource){
		REST.put('/products', resource.id, resource, function(response){
			$state.go('products');
		});
	};
	$scope.clearAttributes = function(product){
		product.price = 0;
		product.average_price = 0;
	}

	$scope.calcAveragePrice = function(product){
		product.average_price = utilsFactory.getAveragePrice(product);
	}
})
.controller('purchaseCtrl', function($scope, $state, REST, utilsFactory) {
	$scope.hashStringToColor = utilsFactory.hashStringToColor;
	$scope.newPurchases = [{}]
	$scope.addFormTuple = function(newPurchases){
		newPurchases.push({}); //just a new element to expand the loop
	};
	$scope.calcTotalPartial = function(purchase){
		var productId = purchase.product,
			product = $scope.products.find(function(product){
				return product.id == productId;
			});
		//set partial total_price
		purchase.total_price = purchase.quantity * product.price;
		//set cart total_price
		//aqui ta o erro
		$scope.cart.total_price = $scope.newPurchases.reduce(function(memo, purchase){
			return memo += purchase.total_price;
		}, 0);
	};
	$scope.clearAttributes = function(purchase){
		purchase.quantity = 0;
		purchase.total_price = 0;
		$scope.cart.total_price = $scope.newPurchases.reduce(function(memo, purchase){
			return memo += purchase.total_price;
		}, 0);
	}
	$scope.getProduct = function(productId){
		if($scope.products !== undefined){
			return $scope.products.find(function(product){
				return product.id == productId;
			});
		}
	}
	//dar um jeito nisso
	REST.getAll('/purchases', function(purchases){
		$scope.purchases = purchases;
	});
	REST.getAll('/products', function(products){
		$scope.products = products;
	});
	$scope.processPurchases = function(newPurchases){
		for (var i = newPurchases.length - 1; i >= 0; i--) {
			if(i == 0){ // no good, last element run the callback
				REST.post('/purchases', newPurchases[i], function(){
					$state.go('purchases');
				});
				return;
			}
			REST.post('/purchases', newPurchases[i]);
		};
	};
	$scope.create = function(resource){
		REST.post('/purchases', resource, function(response){
			$state.go('purchases');
		});
	};
	$scope.update = function(resource){
		REST.put('/purchases', resource.id, resource, function(response){
			$state.go('purchases');
		});
	};
})