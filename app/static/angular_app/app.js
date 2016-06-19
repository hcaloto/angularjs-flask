'use strict';
// Declare app level module which depends on filters, and services
var app= angular.module('myApp', ['ngRoute']);
app.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/login',
			{ templateUrl: 'angular_app/login/partials/login.html',
			  controller: 'loginCtrl'
			});
    $routeProvider.when('/register',
			{ templateUrl: 'angular_app/login/partials/register.html',
			  controller: 'loginCtrl'
			});
    $routeProvider.when('/flask',
			{ templateUrl: 'angular_app/flask/partials/flask.html',
			  controller: 'flaskCtrl',
			  resolve: {
			      load: function($q, loginService){
				  var defer = $q.defer();

				  if (loginService.islogged()){
				      defer.resolve();
				  }else{
				      defer.reject("not_logged_in");
				  }
				  return defer.promise;

			      }
			  }
			});
    $routeProvider.when('/angular',
			{ templateUrl: 'angular_app/angular/partials/angular.html',
			  controller: 'angularCtrl',
			  resolve: {
			      load: function($q, loginService){
				  var defer = $q.defer();
				  if (loginService.islogged()){
				      defer.resolve();
				  }else{
				      defer.reject("not_logged_in");
				  }

				  return defer.promise;
			      }
			  }
			});
    $routeProvider.when('/bootstrap',
			{ templateUrl: 'angular_app/bootstrap/partials/bootstrap.html',
			  controller: 'bootstrapCtrl',
			  resolve: {
			      load: function($q, loginService){
				  var defer = $q.defer();
				  if (loginService.islogged()){
				      defer.resolve();
				  }else{
				      defer.reject("not_logged_in");
				  }
				  return defer.promise;

			      }
			  }
			});
  $routeProvider.otherwise({ redirectTo: '/login' });
}]);


app.run(function($rootScope, $location, loginService){
    var routespermission=['/flask', '/angular', '/bootstrap'];  //route that require login

    $rootScope.$on('$routeChangeStart', function(event, next, current){
	$rootScope.loading = true;

	// Check for login if proceeds
	if(routespermission.indexOf($location.path()) !=-1){
	    if (!loginService.islogged()){
	    	$location.path('/login');
		$rootScope.errortxt='Sorry, the token has expired';
	    }
	}else{
	    console.log($location.path());
	}

    });
});
