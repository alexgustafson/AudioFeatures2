from rest_framework import serializers
from af_documentation.models import Section, ContentNode
from djangoplugins.models import Plugin

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        lookup_field = 'uuid'


class ContentNodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ContentNode
        lookup_field = 'uuid'


class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plugin
        lookup_field = 'uuid'
