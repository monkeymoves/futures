# tools/admin.py
from django.contrib import admin
from .models import Project, Pathway, Tool, HorizonScan, Pestle

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    prepopulated_fields = {'slug': ('title',)}

class PathwayAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class HorizonScanAdmin(admin.ModelAdmin):
    list_display = ('project', 'updated_at')
    search_fields = ('project__title',)

class PestleAdmin(admin.ModelAdmin):
    list_display = ('project', 'updated_at')
    search_fields = ('project__title',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Pathway, PathwayAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(HorizonScan, HorizonScanAdmin)
admin.site.register(Pestle, PestleAdmin)
