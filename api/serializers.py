from rest_framework import serializers
from .models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = '__all__'
        read_only_fields = ['short_code', 'created_at', 'updated_at', 'access_count']
