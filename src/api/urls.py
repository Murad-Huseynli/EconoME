from django.urls import path, include

urlpatterns = [
    path("deals/", include("deals.api_urls")),
]