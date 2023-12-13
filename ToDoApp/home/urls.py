from django.contrib import admin
from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('home/',views.home, name='home'),
    path('edit/<id>', views.edit, name='edit'),
    path('completed/<id>', views.completed, name='completed'),
    path('delete/<id>',views.delete, name='delete'),
    path('priority/<choice>/', views.priority, name='priority'),
    path('status/<choice>/', views.status, name='status'),
    path('', views.signup,name='signup'),
    path('loginn', views.loginn,name='loginn'),
    path('logout/', views.logout, name='logout'),
]