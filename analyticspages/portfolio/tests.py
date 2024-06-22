import pytest
from .models import Project
from django.urls import reverse
from django.contrib.admin.sites import AdminSite
from .admin import ProjectAdmin

# Test for creating a project instance and verifying its attributes
@pytest.mark.django_db
def test_project_create():
    project = Project.objects.create(
        title = 'Test Project',
        description = 'Test Description',
        technology = 'Test Technology',
        image = 'images/test.jpg'
    )
    assert project.title == 'Test Project'
    assert project.description == 'Test Description'
    assert project.technology == 'Test Technology'

# Test for the project_list view to ensure that it returns a 200 status code and contains 'Projects' in the response content
@pytest.mark.django_db
def test_project_list_view(client):
    url = reverse('project_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Projects' in response.content.decode()

# `admin_site` fixture creates an instance of the `AdminSite` class
@pytest.fixture
def admin_site():                   
    return AdminSite()

# `project_admin` fixture creates an instance of the `ProjectAdmin` class using the `admin_site` fixture
@pytest.fixture
def project_admin(admin_site):      
    return ProjectAdmin(Project, admin_site)

# Test to check that the `list_display` attribute of the `ProjectAdmin` class is set correctly
@pytest.mark.django_db
def test_project_admin_list_display(project_admin):         
    assert project_admin.list_display == ('title', 'technology', 'description')