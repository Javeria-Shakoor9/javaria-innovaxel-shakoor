from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer

class CreateShortURL(APIView):
    """Create a new short URL"""
    def post(self, request):
        serializer = ShortenedURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveOriginalURL(APIView):
    """Retrieve the original URL and redirect"""
    def get(self, request, short_code):
        url_entry = get_object_or_404(ShortenedURL, short_code=short_code)
        url_entry.access_count += 1
        url_entry.save()
        return redirect(url_entry.url)

class UpdateShortURL(generics.UpdateAPIView):
    """Update an existing short URL"""
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
    lookup_field = "short_code"

class DeleteShortURL(generics.DestroyAPIView):
    """Delete an existing short URL"""
    queryset = ShortenedURL.objects.all()
    lookup_field = "short_code"

class GetURLStats(APIView):
    """Get statistics for a short URL"""
    def get(self, request, short_code):
        url_entry = get_object_or_404(ShortenedURL, short_code=short_code)
        serializer = ShortenedURLSerializer(url_entry)
        return Response(serializer.data, status=status.HTTP_200_OK)
