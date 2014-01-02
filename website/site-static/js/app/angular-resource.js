
app.factory('Sections', ['$resource', 'urls',
    function ($resource, urls) {
        return $resource(
            urls.section + '/:uuid',
            {uuid: '@uuid'},
            { update: { method: 'PUT' } }
        );
    }]);

app.factory('Content', ['$resource', 'urls',
    function ($resource, urls) {
        return $resource(
            urls.content + ':uuid',
            {uuid: '@uuid'},
            { update: { method: 'PUT'}}
        );
    }]);