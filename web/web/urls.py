from django.contrib import admin
from django.urls import include, path
from semut.views import *

urlpatterns = [
    path('', mk, name='mk'),
    path('mr/',mr, name='mr'),
    path('admin/', admin.site.urls),
]
