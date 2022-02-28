from django.urls import path

from .import views

app_name = 'money'

urlpatterns = [
    path('send/', views.send, name='send'),
    path('success/', views.success, name='success'),
]