from django.shortcuts import render
from af_documentation.models import Section
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from af_documentation.models import Section, ContentNode
from af_documentation.serializers import SectionSerializer, ContentNodeSerializer

def home(request):

    return render(request,
                  'af_documentation/home.html',
                  {
                      'nodes': Section.objects.all(),
                  })


'''rest stuff'''
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def section_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        section = Section.objects.all()
        serializer = SectionSerializer(section, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def section_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        section = Section.objects.get(pk=pk)
    except Section.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SectionSerializer(section)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SectionSerializer(section, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        section.delete()
        return HttpResponse(status=204)


@csrf_exempt
def contentnode_list(request):

    if request.method == 'GET':
        contentnodes = Section.objects.all()
        serializer = ContentNode(contentnodes, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContentNode(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def contentnode_detail(request, pk):

    try:
        contentnode = ContentNode.objects.get(pk=pk)
    except ContentNode.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ContentNodeSerializer(contentnode)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContentNodeSerializer(contentnode, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        section.delete()
        return HttpResponse(status=204)