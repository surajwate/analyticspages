import pytest
from .models import Project

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