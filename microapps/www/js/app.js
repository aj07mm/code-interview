angular.module('myapp', ['microapps.controllers'])
.constant('globals', {
  apiPath : 'https://test.oppwa.com',
  authentication : {
    userId: '8a8294174b7ecb28014b9699220015cc',
    password : 'sy6KJsT8',
    entityId : '8a8294174b7ecb28014b9699220015ca'
  },
  encoding: 'application/x-www-form-urlencoded; charset=UTF-8',
  pathFormat:  {
    'json' : '/?format=json'
  },
  payment : {
    brands : [
      { id: 1, name: 'VISA'},
      { id: 2, name: 'MASTER'},
      { id: 3, name: 'AMEX'},
      { id: 4, name: 'DISCOVER'},
      { id: 5, name: 'MAESTRO'},
      { id: 6, name: 'VISAELECTRON'},
      { id: 7, name: 'JCB'},
      { id: 8, name: 'HIPERCARD'},
      { id: 9, name: 'CARTEBLEUE'},
      { id: 10, name: 'DANKORT'},
      { id: 11, name: 'DINERS'},
      { id: 12, name: 'VPAY'}
    ],
    types: [
      { id: 1, name: 'PA'},
      { id: 2, name: 'DB'},
      { id: 3, name: 'CD'},
      { id: 4, name: 'CP'},
      { id: 5, name: 'RV'},
      { id: 6, name: 'RF'}
    ],
    currencies: [
      { id: 'EUR', name: 'EUR'},
      { id: 'USD', name: 'USD'}
    ]
  }
  
})
.run(function($http, globals) {
  $http.defaults.headers.common.Authorization = 'Basic YmVlcDpib29w';
});