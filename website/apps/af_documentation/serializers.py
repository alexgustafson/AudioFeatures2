from django.forms import widgets
from rest_framework import serializers
from af_documentation.models import Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'title', )