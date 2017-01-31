app.factory('todo', ['$resource', function($resource) {
	return $resource('/tasks/:id', { id: '@_id' }, {
		update: {
	      method: 'PUT' // this method issues a PUT request
	    }
	});
}]);