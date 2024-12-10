from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

def home(request):
    return render(request, 'index.html')

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
                return redirect('admin-dashboard')  # Redirect to the admin dashboard or desired page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'admin-config/user-admin-forms.html', {'form': form})

def add_project(request):
    return render(request, 'admin-config/admin-add-project.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return render(request, 'admin-config/log-out-admin.html')