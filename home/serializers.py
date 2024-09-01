from rest_framework import serializers
from .models import AdPage

class AdPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdPage
        fields = ['title', 'img', 'status', 'buttons', 'media_type']
