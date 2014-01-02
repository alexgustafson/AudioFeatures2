var app = angular.module('audiofeaturesapp', ['ngCookies', 'ngResource', 'ngRoute'], function () {
})

app.config(function ($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('AppController', [
    '$scope', 'Sections', function ($scope, Sections) {
        $scope.sections = Sections.query()

    }
]);

app.controller('ContentController', ['$scope', '$http', function ($scope, $http) {
    return $http.get($scope.$parent.item).then(function (result) {
        $scope.body = result.data.body
    })

}]);




