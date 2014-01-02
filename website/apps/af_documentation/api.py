from af_documentation.models import Section, ContentNode
from af_documentation.serializers import SectionSerializer, ContentNodeSerializer, ContentTypeSerializer
from rest_framework import generics
from djangoplugins.models import Plugin


class SectionList(generics.ListCreateAPIView):
    model = Section
    serializer_class = SectionSerializer


class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Section
    serializer_class = SectionSerializer
    lookup_field = 'uuid'


class ContentNodeList(generics.ListCreateAPIView):
    model = ContentNode
    serializer_class = ContentNodeSerializer


class ContentNodeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ContentNode
    serializer_class = ContentNodeSerializer
    lookup_field = 'uuid'


class ContentTypeList(generics.ListCreateAPIView):
    model = Plugin
    serializer_class = ContentTypeSerializer


class ContentTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Plugin
    serializer_class = ContentTypeSerializer
    lookup_field = 'uuid'

