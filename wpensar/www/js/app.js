angular.module('myapp', ['desafio.controllers', 'desafio.factories', 'desafio.services', 'desafio.directives', 'ui.router', 'angularUtils.directives.dirPagination'])
.constant('globals', {
  'apiPath' : 'http://localhost:8000',
  'pathFormat':  {
    'json' : '/?format=json'
  }
})
//router
.config(function($stateProvider, $urlRouterProvider, $locationProvider) {
  // ===== ROUTES ======
  $stateProvider
  // ------- PRODUCTS -------- //
  .state('products', {
    url: '/products',
    // abstract: true,
    templateUrl: 'templates/product/index.html'
  })
  .state('productsUpdate', {
    url: '/products/edit/:productId',
    templateUrl: 'templates/product/edit.html',
    controller: function ($scope, $stateParams, REST) {
      var productId = parseInt($stateParams.productId);
      REST.get('/products', productId, function(product){
          $scope.product = product;
      });
    }
  })
  .state('productsNew', { //new/create non rails like, create goes on controller.create
    url: '/products/new',
    // abstract: true,
    templateUrl: 'templates/product/new.html'
  })
  .state('productsView', {
    url: '/products/:productId',
    templateUrl: 'templates/product/view.html',
    controller: function ($scope, $stateParams, REST) {
      var productId = $stateParams.productId;
      REST.get('/products', productId, function(product){
          $scope.product = product;
      });
    }
  })
  // .state('products.delete', { 
  //   url: '/:productId',
  //   onEnter: function($state, $stateParams, REST) {
  //     if($stateParams.productId){
  //       var productId = parseInt($stateParams.productId);
  //       REST.delete('/products/' + productId, function(response){
  //         $state.go('products');
  //       })
  //     }
  //   }
  // })


  // ------- PURCHASES -------- //
  .state('purchases', {
    url: '/purchases',
    // abstract: true,
    templateUrl: 'templates/purchase/index.html'
  })
  .state('purchasesUpdate', {
    url: '/purchases/:purchaseId/edit',
    templateUrl: 'templates/purchase/edit.html',
    controller: function ($scope, $stateParams, REST) {
      var purchaseId = $stateParams.purchaseId;
      REST.get('/purchases', purchaseId, function(purchase){
          $scope.purchase = purchase;
      });
    }
  })
  .state('purchasesDelete', { 
    url: '/purchases/:purchaseId/delete',
    templateUrl: 'templates/purchase/index.html', // just to remove glitch
    onEnter: function($state, $stateParams, REST) {
      if($stateParams.purchaseId){
        var purchaseId = $stateParams.purchaseId;
        REST.delete('/purchases/' + purchaseId, function(response){
          $state.go('purchases');
        })
      }
    }
  })
  .state('purchasesNew', { //new/create non rails like, create goes on controller.create
    url: '/purchases/new',
    // abstract: true,
    templateUrl: 'templates/purchase/new.html',
    controller: function($scope, utilsFactory){
      $scope.cart = {}
      $scope.cart.total_price = 0;
      $scope.cart.uuid = utilsFactory.guid();
    }
  })
  .state('purchasesView', {
    url: '/purchases/:purchaseId',
    templateUrl: 'templates/purchase/view.html',
    controller: function ($scope, $stateParams, REST) {
      var purchaseId = $stateParams.purchaseId;
      REST.get('/purchases', purchaseId, function(purchase){
          $scope.purchase = purchase;
      });
    }
  })

  // use the HTML5 History API
  //  $locationProvider.html5Mode(true);
  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/');

});
