from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.contrib.auth.views import LoginView, LogoutView # Import the `LoginView` and `LogoutView` classes to create views for user login and logout
from django.urls import reverse_lazy    # Import the `reverse_lazy` function to redirect users to a URL after successful login
from django.contrib.auth.forms import UserCreationForm  # Import the `UserCreationForm` class to create a form for user registration
from django.views.generic.edit import CreateView    # Import the `CreateView` class to create a view for user registration
from django.contrib import messages # Import the `messages` framework to display messages to users
from django.contrib.auth.mixins import LoginRequiredMixin    # Import the `LoginRequiredMixin` class to restrict access to authenticated users
from django.views.generic import TemplateView   # Import the `TemplateView` class to create a view for user profile
from .forms import ProjectForm
from django.core.paginator import Paginator
from django.db.models import Q

# Function-based view to display a list of all projects
def project_list(request):
    query = request.GET.get('q')
    technology_filter = request.GET.get('technology')
    projects = Project.objects.all().order_by('start_date')
    if query:
        projects = projects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(technology__icontains=query)
        )
    if technology_filter:
        projects = projects.filter(technology__iexact=technology_filter)
    paginator = Paginator(projects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    technologies = Project.objects.values_list('technology', flat=True).distinct()
    return render(request, 'portfolio/project_list.html', {
        'page_obj': page_obj,
        'projects': page_obj.object_list,
        'query': query,
        'technology_filter': technology_filter,
        'technologies': technologies
    })

# Function-based view to display the details of a specific project
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

# Class-based view for user login
class CustomLoginView(LoginView):
    template_name = 'portfolio/login.html'
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
    
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio/profile.html'

    
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/project_form.html', {'form': form})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk = project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio/project_form.html', {'form': form})