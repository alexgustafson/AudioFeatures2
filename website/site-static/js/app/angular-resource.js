var sectionServices = angular.module('sectionServices', ['ngResource'])

sectionServices.factory('Sections', ['$resource',
    function($resource) {
        return $resource('/restdocs/sections', {}, {
            query: {method: 'GET', params:{}, isArray:true}
        });
}])

