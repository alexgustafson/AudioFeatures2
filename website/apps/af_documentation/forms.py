from django import forms
from djangular.forms import NgFormValidationMixin, NgModelFormMixin

from af_documentation.models import Section, ContentNode

class SectionForm(NgModelFormMixin, NgFormValidationMixin, forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title',  ]