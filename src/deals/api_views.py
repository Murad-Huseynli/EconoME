from rest_framework import generics, filters
from .models import Deal
from .serializers import DealSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DealListAPIView(generics.ListAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['endDate', '']
    search_fields = ['title', 'description']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'total': count, 'products': serializer.data})
