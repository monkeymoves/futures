# tools/models.py
from django.db import models # Changed import
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify
#from django.contrib.postgres.fields import JSONField # Removed this import

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
    data = models.JSONField(null=True, blank=True) # Changed field definition

    def get_absolute_url(self):
        """
        Returns the URL for this tool within a specific project.
        """
        if self.project:
            project_slug = self.project.slug
            if self.name == "delphi":
                return reverse("project_delphi", kwargs={"project_slug": project_slug})
            elif self.name == "seven_questions":
                return reverse("project_seven_questions", kwargs={"project_slug": project_slug})
            elif self.name == "three_horizons":
                return reverse("project_three_horizons", kwargs={"project_slug": project_slug})
            elif self.name == "driver_mapping":
                return reverse("project_driver_mapping", kwargs={"project_slug": project_slug})
            elif self.name == "swot":
                return reverse("project_swot", kwargs={"project_slug": project_slug})
            elif self.name == "scenarios":
                return reverse("project_scenarios", kwargs={"project_slug": project_slug})
            elif self.name == "visioning":
                return reverse("project_visioning", kwargs={"project_slug": project_slug})
            elif self.name == "futures_wheels":
                return reverse("project_futures_wheels", kwargs={"project_slug": project_slug})
            elif self.name == "policy_stress_testing":
                return reverse("project_policy_stress_testing", kwargs={"project_slug": project_slug})
            elif self.name == "roadmapping":
                return reverse("project_roadmapping", kwargs={"project_slug": project_slug})
            elif self.name == "backcasting":
                return reverse("project_backcasting", kwargs={"project_slug": project_slug})
            elif self.name == "pestle":
                return reverse("project_pestle", kwargs={"project_slug": project_slug})
            elif self.name == "horizon_scanning":
                return reverse("project_horizon_scanning", kwargs={"project_slug": project_slug})
            else:
                return None  # Or raise an exception if you prefer
        else:
            return None

    def __str__(self):
        return self.name
