from django.shortcuts import render, get_object_or_404
from .models import Project
from django.contrib.auth.views import LoginView, LogoutView # Import the `LoginView` and `LogoutView` classes to create views for user login and logout
from django.urls import reverse_lazy    # Import the `reverse_lazy` function to redirect users to a URL after successful login
from django.contrib.auth.forms import UserCreationForm  # Import the `UserCreationForm` class to create a form for user registration
from django.views.generic.edit import CreateView    # Import the `CreateView` class to create a view for user registration
from django.contrib import messages # Import the `messages` framework to display messages to users

# Function-based view to display a list of all projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

# Function-based view to display the details of a specific project
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

# Class-based view for user login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

# Class-based view for user logout
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('project_list')

# Class-based view for user registration
class RegisterView(CreateView):
    template_name = 'portfolio/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super().form_valid(form)
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Account created for {username}')   # Use the `messages` framework to display messages to users
        return valid