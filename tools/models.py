from django.db import models

# Create your models here.
# tools/models.py

class Pathway(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Many-to-many if a Tool can belong to multiple Pathways
    pathways = models.ManyToManyField(Pathway, related_name='tools')

    def __str__(self):
        return self.name