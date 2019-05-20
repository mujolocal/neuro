from django.urls import path
from django.contrib import admin
from .views import MoodCreateViewset, list_percent_view



urlpatterns = [
    path("",list_percent_view ),
    path("create/",MoodCreateViewset.as_view())
    ]
