from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _
from common_utils.behaviors import Translatable, Timestampable
from djangoplugins.fields import PluginField
from af_documentation.plugins import AfContentType



class Section(MPTTModel, Translatable, Timestampable):
    title = models.CharField(_('Title'), max_length=120,)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertaion_by = ['title']

    def __unicode__(self):
        return "%s" % self.title


class ContentNode(models.Model):
    parent_section = models.ForeignKey('Section', null=True, blank=True, related_name='Content')
    body = models.TextField(default='')
    content_type = PluginField(AfContentType)