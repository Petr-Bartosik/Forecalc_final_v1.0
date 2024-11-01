from django.urls import path
from django.contrib.auth import views as auth_views  # Přidejte tento import
from . import views


urlpatterns = [
    path('', views.uvodni_stranka, name='uvodni_stranka'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/register/', views.registrace, name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('menu/', views.menu, name='menu'),
    path('novy_zaznam/', views.novy_zaznam, name='novy_zaznam'),
    path('seznam_zaznamu/', views.seznam_zaznamu, name='seznam_zaznamu'),
    path('upravit_zaznam/<int:pk>/', views.upravit_zaznam, name='upravit_zaznam'),
    path('smazat_zaznam/<int:pk>/', views.smazat_zaznam, name='smazat_zaznam'),  # Toto je správný název
]
