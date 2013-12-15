SemArbeit.directive('viewstate', ['$rootScope',
    function($rootScope) {
        return {
            link: function (scope, element, attrs) {
                element.addClass('hide');
                $rootScope.$on('$routeChangeStart', function () {
                    element.addClass('hide');
                })
                $rootScope.$on('routeChangeSuccess', function() {
                    element.removeClass('hide');
                })
                $rootScope.$on('routeChangeError', function() {
                    element.addClass('hide');
                })
            }
        }
    }]
);