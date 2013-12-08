from django.shortcuts import render
from af_documentation.models import Section


def home(request):

    return render(request,
                  'af_documentation/home.html',
                  {
                      'nodes': Section.objects.all(),
                  })