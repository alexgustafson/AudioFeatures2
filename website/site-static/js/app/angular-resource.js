app.factory('Sections', ['djResource', 'urls',
    function (djResource, urls) {
        return djResource(
            urls.section + '/:uuid',
            {uuid: '@uuid'},
            { update: { method: 'PUT' } }
        );
    }
]);

app.factory('Content', ['djResource', 'urls',
    function (djResource, urls) {
        return djResource(
            urls.content + '/:uuid',
            {uuid: '@uuid'},
            { update: { method: 'PUT'}}
        );
    }
]);