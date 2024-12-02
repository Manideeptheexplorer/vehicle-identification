from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UploadHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)
    detected_plate_numbers = models.TextField()  # Add this if not present
    detected_states = models.TextField()        # For state info (optional)

    def __str__(self):
        return self.file_name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_token = models.CharField(max_length=32, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    