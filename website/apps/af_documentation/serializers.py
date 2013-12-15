from rest_framework import serializers
from af_documentation.models import Section, ContentNode
from djangoplugins.models import Plugin

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'title', 'content', 'language', )


class ContentNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentNode
        fields = ('body', 'parent_section', 'content_type',)


class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plugin
        fields = ('name' , 'title', )