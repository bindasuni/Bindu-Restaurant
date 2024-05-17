from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('h', views.home, name='h'),
]
