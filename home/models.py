from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User

# Define your STATUS_CHOICES and MEDIA_CHOICES as before
STATUS_CHOICES = {
    "d": "Draft",
    "p": "Published",
    "w": "Withdrawn",
}

MEDIA_CHOICES = {
    "i" : "image",
    "v" : "video"
}

# Custom function to set the upload path and filename
def user_directory_path(instance, filename):
    # Retrieve the username
    username = instance.user.username if instance.user else 0
    # Format the current date
    date_str = timezone.now().strftime("%Y-%m-%d")
    # Define the path and filename
    return f'home/static/ad_pages_media/{username}_{date_str}{filename}'

class AdPage(models.Model):
    title = models.CharField(max_length=100)
    img = models.FileField(upload_to=user_directory_path)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    buttons = models.BooleanField()
    media_type = models.CharField(max_length=1, choices=MEDIA_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0)  # Assuming each AdPage is associated with a user

    def __str__(self):
        return self.title
    
admin.site.register(AdPage)
