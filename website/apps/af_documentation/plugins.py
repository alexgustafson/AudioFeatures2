from djangoplugins.point import PluginPoint

class AfContentType(PluginPoint):
    """
    Documentation, that describes how plugins can implement this plugin
    point.

    """
    @classmethod
    def render_content(self, content):
        return content


class TextContent(AfContentType):
    name = 'text-content'
    title = "Text Content"


class ImageContent(AfContentType):
    name = 'image-content'
    title = "Image Content"

