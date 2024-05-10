from django.conf import settings
from rest_framework import serializers
from .models import Deal

class DealSerializer(serializers.ModelSerializer):
    preview = serializers.SerializerMethodField()

    def get_preview(self, obj):
        imagePath = obj.preview.url
        return imagePath

    class Meta:
        model = Deal
        fields = ['id', 'title', 'description', 'preview', 'termsConditions', 'startDate', 'endDate', 'isActive', 'discountRateByGroup', 'offeredBy']