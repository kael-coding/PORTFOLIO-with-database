from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, ProjectForm
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def dashboard(request):
    return render(request, 'admin-config/admin-succes.html')

def admin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin-dashboard') 
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'admin-config/user-admin-forms.html', {'form': form})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-project')
    else:
        form = ProjectForm()
    return render(request, 'admin-config/admin-add-project.html', {'form': form})

def list_project(request):
    projects = Project.objects.all()
    return render(request, 'admin-config/admin-list-project.html', {'projects': projects})

def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('list-project')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'admin-config/admin-edit-project.html', {'form': form})

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('list-project')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return render(request, 'admin-config/log-out-admin.html')
