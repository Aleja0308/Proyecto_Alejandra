from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login', auth_views.LoginView.as_view(template_name = 'layouts/login.html'), name="login"),
    path('read_inicio/', views.read_inicio, name="read_inicio"),
    path('add_basica/', views.add_basica, name="add_basica"),
    path('read_basica/', views.read_basica, name="read_basica"),
    path('update_basica/<int:pk>/', views.update_basica, name="update_basica"),
    path('delete_basica/<int:pk>/', views.delete_basica, name='delete_basica'),
    path('add_medica/<int:basica_id>/', views.add_medica, name='add_medica'),
    path('read_medica/', views.read_medica, name="read_medica"),
    path('update_medica/<int:pk>/', views.update_medica, name="update_medica"),
    path('delete_medica/<int:pk>/', views.delete_medica, name='delete_medica'),
    path('add_documento/', views.add_documento, name="add_documento"),
    path('add_genero/', views.add_genero, name="add_genero"),
    path('add_sangre/', views.add_sangre, name="add_sangre"),
    path('add_hijos/', views.add_hijos, name="add_hijos"),
    path('add_estado/', views.add_estado, name="add_estado"),
    path('add_ocupacion/', views.add_ocupacion, name="add_ocupacion"),
    path('logout_session/', views.logout_session, name="logout_session"),
]