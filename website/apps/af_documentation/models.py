from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _
from common_utils.behaviors import Translatable, Timestampable
from djangoplugins.fields import PluginField
from af_documentation.plugins import AfContentType
from django_extensions.db.fields import UUIDField
import reversion


class Section(MPTTModel, Translatable, Timestampable):
    title = models.CharField(_('Title'), max_length=120, )
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    uuid = UUIDField()

    class MPTTMeta:
        order_insertaion_by = ['title']

    def __unicode__(self):
        return "%s" % self.title

    def get_plugins(self):

        plugins = []
        for node in self.content.all():
            plugins.append(node.content_type)

        return plugins

    def get_rendered_content_items(self):

        content_items = []
        for node in self.content.all():
            content_items.append(node.render_content())

        return content_items


#reversion.register(Section)


class ContentNode(models.Model):
    parent_section = models.ForeignKey('Section', null=True, blank=True, related_name='content')
    body = models.TextField(default='')
    content_type = PluginField(AfContentType)
    uuid = UUIDField()


    def render_content(self):
        plugin_model = self.content_type.get_plugin()
        return plugin_model.render_content(self.body)


#reversion.register(ContentNode)