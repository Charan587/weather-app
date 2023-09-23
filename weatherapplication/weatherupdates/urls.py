# here we are import path from in-built django-urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]