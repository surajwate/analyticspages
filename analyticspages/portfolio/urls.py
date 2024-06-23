from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]