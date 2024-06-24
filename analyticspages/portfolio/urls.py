from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView, ProfileView, project_create, project_update
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('create/', project_create, name='project_create'),
    path('update/<int:pk>/', project_update, name='project_update'),
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]