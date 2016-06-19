'use strict';

app.factory('sessionService', ['$http', function($http){
	return{
	    setAuth:function(username, token){
		$http.defaults.headers.common['Token'] = token; // jshint ignore:line
		sessionStorage.setItem('username', username);
		return sessionStorage.setItem('token', token);
	    },
	    set:function(key,value){
		return sessionStorage.setItem(key,value);
	    },
	    get:function(key){
		return sessionStorage.getItem(key);
	    },
	    destroy:function(key){
		$http.defaults.headers.common.Authorization = 'Basic ';
		//$http.post('data/destroy_session.php');
		return sessionStorage.removeItem(key);
	    }
	};
}])
