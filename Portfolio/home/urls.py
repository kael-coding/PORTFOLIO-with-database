from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-admin/', views.admin, name= 'user-admin'),
    path('dashboard-admin/', views.dashboard , name='admin-dashboard'),
    path('add-project/', views.add_project, name='add-project'),
    path('logout/', views.logout_view, name='logout'),

]