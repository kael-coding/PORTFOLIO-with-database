from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-admin/', views.admin, name= 'user-admin'),
    path('dashboard-admin/', views.dashboard , name='admin-dashboard'),
    path('list_project/', views.list_project, name='list-project'),
    path('add-project/', views.add_project, name='add-project'),
    path('edit_project/<int:pk>/', views.edit_project, name='edit-project'),
    path('delete_project/<pk>/', views.delete_project, name='delete-project'),
    path('logout/', views.logout_view, name='logout'),

]