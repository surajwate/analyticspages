import pytest
from .models import Project
from django.urls import reverse

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