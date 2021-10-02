from django import urls
from django.contrib import admin
from django.db import router
from django.http import request
from django.urls import path
from django.urls.conf import include
from . import views 
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r'Form', views.Formvieweset)



urlpatterns = [
    path('api',include(routers.urls)),
    path('api_auth/', include('rest_framework.urls',namespace='rest_framework')),
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services'),
    path("form", views.form, name='booking_form'),
]