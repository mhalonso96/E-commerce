from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path ('criar/', views.Criar.as_view(), 'criar'),
    path ('atualizar/', views.Atualizar.as_view(), 'atualizar'),
    path ('login/', views.Login.as_view(), 'login'),
    path ('logout/', views.Logout.as_view(), 'logout'),
]
