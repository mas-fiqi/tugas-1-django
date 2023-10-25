from django.urls import path
from . import views

urlspatterns = [
    path('semut', views.semut, name='semut')
]