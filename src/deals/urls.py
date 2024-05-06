from django.urls import path, include
from django.contrib.auth import views as authViews
from .views import dealsView

urlpatterns = [
    path('deals', dealsView, name='deals-view')
]
