from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _


LANGUAGES = [
             ('de', 'Deutsch'),
             ('en', 'English'),
             ]

class Section(MPTTModel):
    title = models.CharField(_('Title'), max_length=120,)
    main_text = models.TextField(_('Main Text'), blank=True, null=True)
    order = models.IntegerField(_('Order'), blank=True, null=True)
    language = models.CharField(_('Language'), max_length=2, choices=LANGUAGES, default='en')

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertaion_by = ['name']

    def __unicode__(self):
        return "%s" % self.title


class TextContent(models.Model):
    parent_section = models.ForeignKey(_('Parent Section'), null=True, blank=True, related_name='Text')
    order = models.IntegerField(_('Order'), blank=True, null=True)




class Source(models.Model):
    title = models.CharField(_('Title'), max_length=120,)
    source_ref = models.TextField(_('Source Reference'), blank=True, null=True)