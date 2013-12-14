from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext as _
from common_utils.behaviors import Translatable, Timestampable


CONTENT_TYPES = [
    ('text', 'Text'),
    ('fig', 'Figure'),
    ('process', 'Process'), ]


class Section(MPTTModel, Translatable, Timestampable):
    title = models.CharField(_('Title'), max_length=120,)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertaion_by = ['title']

    def __unicode__(self):
        return "%s" % self.title


class ContentNode(models.Model):
    parent_section = models.ForeignKey('Section', null=True, blank=True, related_name='Content')
    type = models.CharField(_('Content Type'), max_length=10, choices=CONTENT_TYPES, default='text')

    text_content = models.ForeignKey('TextContent')
    figure_content = models.ForeignKey('FigureContent')


class TextContent(models.Model,):
    main_text = models.TextField(_('Main Text'), blank=True, null=True)


class FigureContent(models.Model):
    image = models.ImageField(_('Figure'), null=True, blank=True, upload_to="figures", )


class Source(models.Model):
    title = models.CharField(_('Title'), max_length=120,)
    source_ref = models.TextField(_('Source Reference'), blank=True, null=True)