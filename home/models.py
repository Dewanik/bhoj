from django.db import models
from django.contrib import admin
# Create your models here.


STATUS_CHOICES = {
    "d": "Draft",
    "p": "Published",
    "w": "Withdrawn",
}

MEDIA_CHOICES = {
   "i": "image",
    "v":"video"
}

class AdPage(models.Model):
    title = models.CharField(max_length=100)
    img = models.FileField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    buttons = models.BooleanField()
    media_type = models.CharField(max_length=1,choices=MEDIA_CHOICES)
    def __str__(self):
        return self.title
    
admin.site.register(AdPage)