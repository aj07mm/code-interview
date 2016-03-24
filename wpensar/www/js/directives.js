angular.module('desafio.directives', [])
.directive('loading',   ['$http' , function ($http, $scope){
    return {
        restrict: 'A',
        link: function ($scope, elm, attrs){
            $scope.isLoading = function () {
                return $http.pendingRequests.length > 0;
            };
            $scope.$watch($scope.isLoading, function (v) {
                if(v){
                    console.log('done!');
                    elm[0].style.display = "block";
                }else{
                    console.log('loading...');
                    elm[0].style.display = "none";
                }
            });
        }
    };

}]);