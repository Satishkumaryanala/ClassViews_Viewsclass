"""
URL configuration for project_ClassViews_CBV project.

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
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('FBV_String/',FBV_String,name='FBV_String'),
    path('CBV_String/',CBV_String.as_view(),name='CBV_String'),

    path('FBV_page/',FBV_page,name='FBV_page'),
    path('CBV_page/',CBV_page.as_view(),name='CBV_page'),

    path('FBV_insert/',FBV_insert,name='FBV_insert'),
    path('CBV_insert/',CBV_insert.as_view(),name='CBV_insert'),

    path('CBV_TempView/',CBV_TempView.as_view(),name='CBV_TempView'),
]
