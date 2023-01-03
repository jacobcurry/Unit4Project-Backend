from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=32)
    title = models.CharField(max_length=40)
    formBody = models.CharField(max_length=300)
    imageURL = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
