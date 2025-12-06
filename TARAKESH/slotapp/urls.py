from django.urls import path
from slotapp import views
from django.contrib import admin
from django.views.generic import TemplateView
urlpatterns = [
    path('time/', views.time_view, name='time'),
    
    path('',TemplateView.as_view(template_name="slothome.html"),name="slothome"),
]    