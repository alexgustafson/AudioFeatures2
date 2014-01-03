var app = angular.module('audiofeaturesapp', ['ngCookies', 'djangoRESTResources', 'ngRoute', 'ngResource', 'ngSanitize'], function () {
})

app.config(function ($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('SectionListController', [
    '$scope', 'Sections', function ($scope, Sections) {
        $scope.sections = Sections.query()
    }
]);

app.controller('SectionItemController', [
    '$scope', 'Sections', function ($scope, Sections) {

        $scope.show_edit = function () {
            if($scope.show_edit_panel) {
                $scope.show_edit_panel = false;
            }else {
                $scope.show_edit_panel = true;
            }
        }

        $scope.update = function () {
            Sections.update(this.section)
            $scope.show_edit();
        }
    }
]);

app.controller('ContentController', [
    '$scope', 'Content', function ($scope, Content) {
        $scope.content = Content.get({ uuid:$scope.$parent.item})

        $scope.show_edit = function () {

            alert('edit');
        }
}]);

app.directive('ngSectionform', ['urls',
    function(urls) {
        return {
            restrict : 'A',
            templateUrl: urls.sectionForm
        }
    }
]);



