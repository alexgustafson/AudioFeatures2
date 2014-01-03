from rest_framework import serializers
from af_documentation.models import Section, ContentNode
from djangoplugins.models import Plugin

class SectionSerializer(serializers.ModelSerializer):
    content = serializers.SlugRelatedField(many=True, slug_field='uuid')

    class Meta:
        model = Section
        lookup_field = 'uuid'


class ContentNodeSerializer(serializers.ModelSerializer):

    rendered_content = serializers.SerializerMethodField('render_content')

    class Meta:
        model = ContentNode
        lookup_field = 'uuid'

    def render_content(self, obj):
        return obj.render_content()


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plugin
        lookup_field = 'uuid'
