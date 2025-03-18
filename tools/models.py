# tools/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    pathways = models.ManyToManyField('Pathway', related_name='projects', blank=True)  # Add this line
    tools = models.ManyToManyField('Tool', related_name='projects', blank=True)  # Add this line

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Pathway(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    pathways = models.ManyToManyField(Pathway, related_name='tools', blank=True)

    def __str__(self):
        return self.name

class HorizonScan(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='horizon_scan')
    input_data = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Horizon Scan for {self.project.title} (updated: {self.updated_at})"

class Pestle(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='pestle')
    political = models.TextField(null=True, blank=True)
    economic = models.TextField(null=True, blank=True)
    social = models.TextField(null=True, blank=True)
    technological = models.TextField(null=True, blank=True)
    legal = models.TextField(null=True, blank=True)
    environmental = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PESTLE Analysis for {self.project.title}"
