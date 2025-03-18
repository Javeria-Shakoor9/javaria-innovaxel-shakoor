import random
import string
from django.db import models

def generate_unique_short_code():
    """Generate a unique random short code"""
    while True:
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if not ShortenedURL.objects.filter(short_code=short_code).exists():
            return short_code

class ShortenedURL(models.Model):
    url = models.URLField(unique=True)  # Original URL
    short_code = models.CharField(max_length=10, unique=True, default=generate_unique_short_code)  # Unique short code
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)  # Tracks access count

    def __str__(self):
        return f"{self.short_code} -> {self.url}"
