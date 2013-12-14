from django.forms import widgets
from rest_framework import serializers
from af_documentation.models import Section, ContentNode

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'title', 'Content', )

class ContentNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentNode
        fields = ('body', 'content_type')