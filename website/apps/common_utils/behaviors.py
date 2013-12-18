from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

class Timestampable(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Translatable(models.Model):
    language = models.CharField(_('Language'), max_length=2, choices=settings.LANGUAGES, default='en')

    class Meta:
        abstract = True