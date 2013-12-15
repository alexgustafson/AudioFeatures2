app.factory 'Sections', ['$resource', ($resource) ->
  $resource '/restdocs/sections/'
]

app.factory 'SectionsContent', ['$resource', ($resource) ->
  $resource '/restdocs/contentnodes/:id', id: '@id'
]
