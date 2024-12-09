from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('manager', views.manager, name='manager'),
    path('add_task', views.add_task, name='add_task'),
    path('toggle_task_status', views.toggle_task_status, name='toggle_task_status'),
]