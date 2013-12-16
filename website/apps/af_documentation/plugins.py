from djangoplugins.point import PluginPoint
from django.template import Context, loader

class AfContentType(PluginPoint):
    """
    Documentation, that describes how plugins can implement this plugin
    point.

    """
    def render_content(self, content):
        t = loader.get_template('af_documentation/plugins/plugin_wrapper.html')
        c = Context({'content': content,
                     'plugin': self,
                     })
        return t.render(c)


class TextContent(AfContentType):
    name = 'text-content'
    title = "Text Content"


class ImageContent(AfContentType):
    name = 'image-content'
    title = "Image Content"

