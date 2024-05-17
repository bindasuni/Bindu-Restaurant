from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path('c', views.send_email, name='c'),
    path('success', views.send_success, name='success'),
]
