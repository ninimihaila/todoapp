app.directive('task',function(){
  return {
    restrict:'E',
    scope:{
      task:'=task'
    },
    template:'<div ng-style="{\'text-decoration\':task.done?\'line-through\':\'none\'}">'+
    			'<label><input type="checkbox" ng-model="task.done"></input>{{task.description}}</label>'+
    		 '</div>'
  };
});