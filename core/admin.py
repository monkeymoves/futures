from django.contrib import admin
from .models import Project
from .models import Project, Pathway, Tool, UserInput   


# Register your models here.
from .models import Project, Pathway, Tool, UserInput

admin.site.register(Project)
admin.site.register(Tool)
admin.site.register(UserInput)