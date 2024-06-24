from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technology', 'image', 'start_date', 'end_date', 'github_link', 'live_demo_link']