from django.db import models
from auth_api.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User.id, on_delete=models.CASCADE,)
    title = models.CharField(max_length=255)
    formBody = models.TextField(null=True, blank=True)
    imageURL = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
