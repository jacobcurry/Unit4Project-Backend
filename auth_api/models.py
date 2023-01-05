from django.db import models
from django.forms.models import model_to_dict
import json

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        obj = {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'email': self.email,
        }
        return json.dumps(obj)