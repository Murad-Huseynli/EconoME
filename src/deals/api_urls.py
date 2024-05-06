from django.urls import path

from .api_views import DealListAPIView

urlpatterns = [
    path('', DealListAPIView.as_view(), name='list-competitions'),
  
]