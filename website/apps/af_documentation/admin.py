from django.contrib import admin
from models import Section, TextContent, FigureContent, ContentNode
from treeadmin.admin import TreeAdmin


class ContentNodeInline(admin.TabularInline):
    model = ContentNode


class SectionAdmin(TreeAdmin):

    list_display = ('title', 'language', )
    inlines = [
        ContentNodeInline,
    ]



admin.site.register(Section, SectionAdmin)