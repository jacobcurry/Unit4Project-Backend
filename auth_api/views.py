from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = UserSerializer # tell django what serializer to use

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

def check_login(request):
    if request.method=='Get':
        return JsonResponse({})

    if request.method=='PUT':
        jsonRequest = json.loads(request.body)
        email = jsonRequest['email']
        password = jsonRequest['password']
        if User.objects.get(email=email):
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return JsonResponse({'id': user.id, 'firstname': user.firstname, 'lastname': user.lastname, 'email': user.email, 'username': user.username})
            else:
                return JsonResponse({'error' : 'password does not match'})
        else:
            return JsonResponse({'error' : 'email does not exist'})