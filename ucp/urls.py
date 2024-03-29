"""
URL configuration for smartsubmitucp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home),
    path("login_user", views.login_view , name='login_user'),
    path("feed", views.feed , name='feed'),
    path("assignment", views.assignment),
    path("profile", views.profile ,name='profile'),
    path('logout', views.delete_session, name='logout'),
    path('testing', views.testing, name='examplet'),
    path('delete_session/', views.delete_session, name='delete_session'),
     path('accounts/login/', views.show_logged_out, name='show_logged_out'),
    path('', views.upload_assignment, name='upload_assignment'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)