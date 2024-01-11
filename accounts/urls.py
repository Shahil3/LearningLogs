"""Defines url pattern for accounts"""

from django.urls import path,include
from . import views
from django.contrib.auth import logout

app_name = 'accounts'

urlpatterns = [
    #include default auth urls
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name = 'register'),
]
