from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main-home'),
    path('about-us', views.about_us, name='main-about-us'),
    path('in-development', views.in_development, name='in-development-status')
]