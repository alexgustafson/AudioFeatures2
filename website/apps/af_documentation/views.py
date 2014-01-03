from django.shortcuts import render
from af_documentation.forms import SectionForm, ContentNode


def home(request):
    return render(request,
                  'af_documentation/home_angular.html',
        {
        })

def section_form(request):
    form = SectionForm(scope_prefix='section')

    return render(request, 'af_documentation/partials/formholder.html', {
        'form': form,
    })


def rendercontent(request, uuid=None):
    content_node = ContentNode.objects.get(uuid=uuid)

    return render(request, 'af_documentation/plugins/plugin_wrapper.html', {
        'content': content_node.render_content(),
    })