from rest_framework import serializers
from .models import AdPage, CateringCategory

class AdPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdPage
        fields = ['title', 'img', 'status', 'buttons', 'media_type']

class CateringCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CateringCategory
        fields = ['title','value']