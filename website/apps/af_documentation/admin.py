from django.contrib import admin
from models import Section
from treeadmin.admin import TreeAdmin

class SectionAdmin(TreeAdmin):

    list_display = ('title', 'language', )

admin.site.register(Section, SectionAdmin)