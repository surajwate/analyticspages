import pytest
from .models import Project
from django.urls import reverse
from django.contrib.admin.sites import AdminSite
from .admin import ProjectAdmin
from django.contrib.auth.models import User

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

# Test for the project_detail view to ensure that it returns a 200 status code and contains the project title in the response content
@pytest.mark.django_db
def test_project_detail_view(client, project):
    url = reverse('project_detail', kwargs={'pk': project.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert project.title in response.content.decode()

# Fixture to create a sample project for testing    
@pytest.fixture
def project():
    return Project.objects.create(
        title='Test Project',
        description='Test Description',
        technology='Test Technology',
        image='images/test.jpg'
    )

@pytest.mark.django_db
def test_static_files_served(client):
    url = reverse('project_list')   # Use the URL of a view that serves static files
    response = client.get(url)
    assert response.status_code == 200
    assert 'style.css' in response.content.decode()  # Check if the CSS file is included in the response content

@pytest.mark.django_db
def test_media_files_served(client, project):
    # Create a test project with an image to test serving media files
    url = reverse('project_detail', kwargs={'pk': project.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert project.image.url in response.content.decode()  # Check if the image URL is included in the response content

@pytest.fixture
def project():
    return Project.objects.create(
        title='Test Project',
        description='Test Description',
        technology='Test Technology',
        image='images/housing.jpg'  # Ensure the image file exists in the 'media/images' directory of the project
    )

@pytest.mark.django_db
def test_register(client):
    url = reverse('register')
    response  = client.get(url)
    assert response.status_code == 200
    data = {
        'username': 'testuser',
        'password1': 'complexpassword123',
        'password2': 'complexpassword123'
    }
    response = client.post(url, data)
    assert response.status_code == 302 # Redirect after successful registration
    assert User.objects.filter(username='testuser').exists() # Check if the user was created successfully

@pytest.mark.django_db
def test_login(client):
    User.objects.create_user(username='testuser', password='complexpassword123')
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    data = {
        'username': 'testuser',
        'password': 'complexpassword123'
    }
    response = client.post(url, data)
    assert response.status_code == 302

@pytest.mark.django_db
def test_logout(client, django_user_model):
    testuser = django_user_model.objects.create_user(username='testuser', password='complexpassword123')
    client.login(username='testuser', password='complexpassword123')
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302