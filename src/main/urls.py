from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main-home'),
    path('in-development', views.in_development, name='in-development-status')
]