import pytest
from .models import Project
from django.urls import reverse
from django.contrib.admin.sites import AdminSite
from .admin import ProjectAdmin

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

@pytest.mark.django_db
def test_project_list_view(client):
    url = reverse('project_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Projects' in response.content.decode()

@pytest.fixture
def admin_site():                   # `admin_site` fixture creates an instance of the `AdminSite` class
    return AdminSite()

@pytest.fixture
def project_admin(admin_site):      # `project_admin` fixture creates an instance of the `ProjectAdmin` class using the `admin_site` fixture
    return ProjectAdmin(Project, admin_site)

@pytest.mark.django_db
def test_project_admin_list_display(project_admin):         # This test checks that the `list_display` attribute of the `ProjectAdmin` class is set correctly
    assert project_admin.list_display == ('title', 'technology', 'description')