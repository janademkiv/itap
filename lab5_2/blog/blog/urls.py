"""
URL configuration for blog project.

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
from articles import views
from django.urls import include
from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views



urlpatterns = [
    re_path(r'^article/(?P<article_id>\d+)$', views.get_article, name='get_article'),
    path('articles/', views.archive, name='archive'),
    path('', views.archive, name='archive'),
    path('admin/', admin.site.urls),
    path('article/new/', views.create_post, name='article_new'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^signup/$', views.sign_up, name='sign_up'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
