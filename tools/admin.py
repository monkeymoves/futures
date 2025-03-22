# tools/admin.py
from django.contrib import admin
from .models import Project, Tool

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    prepopulated_fields = {'slug': ('title',)}


class ToolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tool, ToolAdmin)
