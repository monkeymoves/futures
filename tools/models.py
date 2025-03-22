# tools/models.py
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tools = models.ManyToManyField('Tool', blank=True, related_name='projects')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Tool(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the URL for this tool within a specific project.
        """
        if self.project:
            project_slug = self.project.slug
            if self.name == "delphi":
                return reverse("delphi", kwargs={"project_slug": project_slug})
            elif self.name == "seven_questions":
                return reverse("seven_questions", kwargs={"project_slug": project_slug})
            elif self.name == "three_horizons":
                return reverse("three_horizons", kwargs={"project_slug": project_slug})
            elif self.name == "driver_mapping":
                return reverse("driver_mapping", kwargs={"project_slug": project_slug})
            elif self.name == "swot":
                return reverse("swot", kwargs={"project_slug": project_slug})
            elif self.name == "scenarios":
                return reverse("scenarios", kwargs={"project_slug": project_slug})
            elif self.name == "visioning":
                return reverse("visioning", kwargs={"project_slug": project_slug})
            elif self.name == "futures_wheels":
                return reverse("futures_wheels", kwargs={"project_slug": project_slug})
            elif self.name == "policy_stress_testing":
                return reverse("policy_stress_testing", kwargs={"project_slug": project_slug})
            elif self.name == "roadmapping":
                return reverse("roadmapping", kwargs={"project_slug": project_slug})
            elif self.name == "backcasting":
                return reverse("backcasting", kwargs={"project_slug": project_slug})
            elif self.name == "pestle":
                return reverse("pestle", kwargs={"project_slug": project_slug})
            elif self.name == "horizon_scanning":
                return reverse("horizon_scanning", kwargs={"project_slug": project_slug})
            else:
                return None  # Or raise an exception if you prefer
        else:
            return None

    def __str__(self):
        return self.name
