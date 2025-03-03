from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Pathway(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Tool(models.Model):
    pathway = models.ForeignKey(Pathway, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

class UserInput(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    input_data = models.JSONField(default=dict)
    updated_at = models.DateTimeField(auto_now=True)