var app = angular.module('audiofeaturesapp', ['ngCookies', 'djangoRESTResources', 'ngRoute'], function () {
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

app.controller('ContentController', ['$scope', 'Content', function ($scope, Content) {
        $scope.content = Content.query({ uuid:$scope.$parent.item})

}]);




