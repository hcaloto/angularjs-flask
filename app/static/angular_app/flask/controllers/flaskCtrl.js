'use strict';

app.controller('flaskCtrl', ['$rootScope', '$scope', '$location', 'loginService', 'sessionService', function($rootScope, $scope, $location, loginService, sessionService){
    $scope.logout=function(){
	loginService.logout();
    };

    $scope.isActive = function (viewLocation) {
	return viewLocation === $location.path();
    };

    $scope.init = function (){
	if (typeof $scope.globals === "undefined") {
	    $rootScope.globals = {}
	}
	$rootScope.globals.username = sessionService.get('username');
    };
    
    $scope.$on("$routeChangeError", function(evt,current,previous,rejection){
	if(rejection == "not_logged_in"){
	    //DO SOMETHING
	} else {
	    //OR DO SOMETHING ELSE
	}
    });
    
    $scope.init();
    $rootScope.loading = false;

}])
