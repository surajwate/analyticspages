from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    github_link = models.URLField(max_length=200, null=True, blank=True)
    live_demo_link = models.URLField(max_length=200, null=True, blank=True)
    result_summary = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return self.title