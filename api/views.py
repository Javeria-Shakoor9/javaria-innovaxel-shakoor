from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer

class ShortURLView(APIView):
    """Handles GET (Retrieve), PUT (update), DELETE (remove) requests"""

    def get(self, request, short_code):
        """Retrieve the original URL (without redirect)"""
        try:
            url_entry = ShortenedURL.objects.get(short_code=short_code)
            url_entry.access_count += 1  # Increase access count
            url_entry.save()
            
            # Serialize and return full details in JSON format
            serializer = ShortenedURLSerializer(url_entry)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ShortenedURL.DoesNotExist:
            return Response({"error": "Short URL not found."}, status=status.HTTP_404_NOT_FOUND)


    def put(self, request, short_code):
        """Update an existing short URL"""
        try:
            url_entry = ShortenedURL.objects.get(short_code=short_code)
        except ShortenedURL.DoesNotExist:
            return Response({"error": "Short URL not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ShortenedURLSerializer(url_entry, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid data", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, short_code):
        """Delete an existing short URL"""
        try:
            url_entry = ShortenedURL.objects.get(short_code=short_code)
            url_entry.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ShortenedURL.DoesNotExist:
            return Response({"error": "Short URL not found."}, status=status.HTTP_404_NOT_FOUND)

class CreateShortURL(APIView):
    """Create a new short URL"""
    def post(self, request):
        serializer = ShortenedURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetURLStats(APIView):
    """Get statistics for a short URL"""
    def get(self, request, short_code):
        url_entry = get_object_or_404(ShortenedURL, short_code=short_code)
        serializer = ShortenedURLSerializer(url_entry)
        return Response(serializer.data, status=status.HTTP_200_OK)
