from django.urls import path
from slotapp import views

urlpatterns = [
    path('', views.time_view, name='time'),
    path('time/', views.time_view, name='time'),
]    