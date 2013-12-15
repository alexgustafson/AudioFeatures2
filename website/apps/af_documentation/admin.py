from django.contrib import admin
from models import Section, ContentNode
from treeadmin.admin import TreeAdmin
import reversion

class ContentNodeInline(admin.TabularInline):
    model = ContentNode


class SectionAdmin(reversion.VersionAdmin, TreeAdmin):

    list_display = ('title', 'language', )
    inlines = [
        ContentNodeInline,
    ]



admin.site.register(Section, SectionAdmin)