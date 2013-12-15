from django.shortcuts import render
from af_documentation.models import Section
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from af_documentation.models import Section, ContentNode
from af_documentation.serializers import SectionSerializer, ContentNodeSerializer, ContentTypeSerializer
from rest_framework import generics
from af_documentation.plugins import AfContentType
from djangoplugins.models import Plugin

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



class SectionList(generics.ListCreateAPIView):
    model = Section
    serializer_class = SectionSerializer


class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Section
    serializer_class = SectionSerializer


class ContentNodeList(generics.ListCreateAPIView):
    model = ContentNode
    serializer_class = ContentNodeSerializer

class ContentNodeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ContentNode
    serializer_class = ContentNodeSerializer

class ContentTypeList(generics.ListCreateAPIView):
    model = Plugin
    serializer_class = ContentTypeSerializer

class ContentTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Plugin
    serializer_class = ContentTypeSerializer

