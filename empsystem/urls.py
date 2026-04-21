"""
URL configuration for empsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include

from emp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base),
    path('home/', views.home),
    path('hrmanager/', views.hr),
    path('employee/', views.employee),
    path('accounts/', include('django.contrib.auth.urls')),
    path('addemp/', views.addemployee, name='addemp'),
    path('viewemployee/', views.viewemployee, name='viewemployee'),
    path('update/<int:pk>/', views.updateview, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('data/', views.export_csv, name='export_csv'),
    path('news/', views.latestnews, name='news'),
    path('detail/<int:pk>/', views.newsdetail, name='detail'),
    path('addnews/', views.addnews, name='addnews'),
    path('newsupdate/<int:pk>/', views.NewsUpdateView.as_view(), name='newsupdate'),
    path('newsdel/<int:pk>/', views.NewsDeleteView.as_view(), name='newsdel'),
    path('cal/', views.calendar, name='cal'),
    path('holidays/', views.holidays, name='holidays'),
    path('job/',views.jobopen,name='job'),
    path('jobdata/', views.viewjob,name='jobdata'),
]


