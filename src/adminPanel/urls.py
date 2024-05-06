from django.urls import path, include
from django.contrib.auth import views as authViews
from .views import requestsView, requestDetail

urlpatterns = [
    path('', requestsView, name='admin-requests-view'),
    path('<int:pk>', requestDetail, name='admin-request-detail')
]
