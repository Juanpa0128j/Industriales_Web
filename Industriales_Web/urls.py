"""Industriales_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Blog_Industriales import views

urlpatterns = [
    path("", views.Hogar, name=""),
    path("Construcciones", views.Construcciones, name="Construcciones"),
    path("Electricidad", views.Electricidad, name="Electricidad"),
    path("Electronica", views.Electronica, name="Electronica"),
    path("Diseno_de_Productos", views.Diseno_de_Productos, name="Diseno_de_Productos")
]
