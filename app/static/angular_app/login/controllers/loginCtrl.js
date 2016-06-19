'use strict';

app.controller('loginCtrl', ['$rootScope', '$scope','loginService', function ($rootScope, $scope,loginService) {
    $scope.login=function(data){
	$rootScope.loading = true;
	var login = loginService.login(data,$scope); //call login service
	login.then(function (data){
	    $scope.errortxt='';
	    $rootScope.loading = false;
	})
	login.error(function (data){
	    $scope.errortxt='Unauthorized, please check your credentials';
	    $rootScope.loading = false;
	})

    };

    $scope.register=function(data){
	      $rootScope.loading = true;
	      console.log(data);
    };

    $rootScope.loading = false;
}]);
