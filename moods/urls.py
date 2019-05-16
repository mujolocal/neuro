from django.urls import path
from django.contrib import admin
from .views import MoodListViewset


urlpatterns = [
    path("", MoodListViewset.as_view() )
]
