from django.urls import path, include
from django.contrib.auth import views as authViews
from .views import dealsView, dealsDetailView

urlpatterns = [
    path('deals', dealsView, name='deals-view'),
    path('deal/<int:pk>', dealsDetailView, name='deals-detail')
]
