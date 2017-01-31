app.controller('TodoController', ['$scope', 'todo', function($scope, todo) {
  $scope.newTodo = '';
  $scope.tasks = todo.query();

  $scope.addTodo = function(){
  	$scope.tasks.push({'description':$scope.newTodo, 'done':false, 'id':0});
  	todo.save($scope.newTodo);
  	$scope.newTodo = '';
  };

  $scope.todoChanged = function(id, done) {
  	alert(id + done)
  }
}]);
