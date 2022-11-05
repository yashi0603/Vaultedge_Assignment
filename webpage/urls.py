from django.contrib import admin
from django.urls import path
from webpage import views

urlpatterns = [
    path("",views.index, name="home"),
    path("compute",views.compute, name="compute")
]