'use strict'

var poll_app = angular.module('pollApp', ['ngRoute', 'ngAnimate']);


poll_app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    });
    
    $routeProvider.when('/', {
        templateUrl: '/static/partials/landing.html'
      }).when('/test', {
        templateUrl: '/static/partials/test.html'
      }).otherwise({
        redirectTo: '/'
      });

  }]);

poll_app.controller('Poll', ['$scope', '$http', '$location', function ($scope, $http, $location) {
    // specify csrf token name and header(django send csrftoken with cookie)
    $http.defaults.xsrfCookieName = 'csrftoken';
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';

    // mark if test finished
    $scope.is_finished = false;

    // mark id data loaded
    $scope.is_loaded = false;

    // get questions for poll with id=1 from the server
    $http.get('/api/poll/1').
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
            $scope.answers_id = Array.apply(0,
                Array($scope.questions.length)).map(function () { return []; });
            // questions loaded
            $scope.is_loaded = true;
        });

    $scope.next = function() {
        if ($scope.current_pos + 1 == $scope.questions.length) {
            $scope.is_loaded = false;
            var total_value = calculate_total_value($scope.answers_id, $scope.questions);
            // send answers to the server
            $http.post('/api/poll_result/save', {total_value: total_value, poll: 1}).
                then(function() {return $http.get('/api/possible_poll_result',
                    {params: {poll_id: 1, total_value: total_value}})}).
                then(function(response) {
                    $scope.poll_result = response.data;
                    $scope.is_finished = true;
                    $scope.is_loaded = true;
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
        try {
            $scope.answers_id = Array.apply(0,
                Array($scope.questions.length)).map(function () { return []; });
            update_btn_name();
        } catch(error) {
            // questions already not loaded
        }
        $location.path('/test');
    };

    // toggle selection for a given answer by his id
    $scope.toggleSelection = function toggleSelection(selected_answer) {
        var index = $scope.answers_id[$scope.current_pos].indexOf(selected_answer);
        // answer already selected
        if (index > - 1) {
            // remove answer
            $scope.answers_id[$scope.current_pos].splice(index, 1);
        } else {
            // select answer
            $scope.answers_id[$scope.current_pos].push(selected_answer);
        }
    };
}]);

function shuffle(array) {
    // function that randomize array elements
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

function calculate_total_value(answers, questions) {
    var total_value = 0;
    for (var i = 0; i < answers.length; i++) {
        var answer_vals = questions[i].answers.map(function(answer, index) {
            return answers[i].indexOf(answer.id) > -1 ? answer.value: 0
        });
        total_value += answer_vals.reduce(function(a, b) { return a + b; }, 0);
    }
    return total_value;
}