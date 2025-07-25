"""
URL configuration for test_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from my_app.views import BookListCreateAPIView
from my_app import views
from django.http import HttpResponse
from django.shortcuts import redirect


def home(request):
    return HttpResponse('<h1 style="color:#0D1C23;"}>Welcome to Dem Bank</h1>')

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        '',
        home
    ),
    path(
        'api/books',
        views.BookListCreateAPIView.as_view(),
        name='book_list_create'
    ),
]
