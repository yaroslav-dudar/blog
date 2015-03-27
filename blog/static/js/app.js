'use strict'

var poll_app = angular.module('pollApp', ['ngRoute', 'ngAnimate']);


poll_app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
	$locationProvider.html5Mode({
	    enabled: true,
	    requireBase: false
	});
	
    $routeProvider.when('/', {
        templateUrl: '/static/partials/landing.html',
        controller: 'Poll'
      }).when('/test', {
        templateUrl: '/static/partials/test.html',
        controller: 'Poll'
      }).otherwise({
        redirectTo: '/'
      });

  }]);

poll_app.controller('Poll', ['$scope', '$http', '$location', function ($scope, $http, $location) {
	// specify csrf token name and header
	$http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';

    $scope.is_finished = false;
    // get guestions for poll with id=1 from the server
	$http.get('/poll/1').
		success(function(data, status, headers, config) {
			$scope.questions = shuffle(data);
			// shuffle answers in all questions
			for (var i = 0; i < $scope.questions.length; i++) {
				$scope.questions[i].answers = shuffle($scope.questions[i].answers);
			}
			if ($scope.questions.length > 0) {
				$scope.current_pos = 0;
				update_btn_name();
			}
			$scope.answers_id = Array($scope.questions.length);
		});

	$scope.next = function() {
		if ($scope.current_pos + 1 == $scope.questions.length) {
			// send answers to the server
			$http.post('/poll/save', {'answers': $scope.answers_id, 'poll': '1'}).
				success(function(data, status, headers, config) {
					$scope.poll_result = data;
					$scope.is_finished = true;
				});
		} else {
			$scope.current_pos++;
			update_btn_name();	
		}
	}

	$scope.previous = function() {
		$scope.current_pos--;
		update_btn_name();
	};

	function update_btn_name() {
		$scope.toggle_text = $scope.current_pos + 1 == $scope.questions.length ? 'Звершити': 'Далі';
	};
	
	$scope.start_test = function () {
		// clear all answers
		$scope.is_finished = false;
		$scope.current_pos = 0;
		$scope.answers_id = Array($scope.questions.length);
		update_btn_name();

		$location.path('/test');
	}
}]);

function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex ;

    while (0 !== currentIndex) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;

      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
    return array;
};