from rest_framework import serializers 
from .models import User 
from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = User # tell django which model to use
        fields = ('id', 'firstname', 'lastname', 'email', 'username', 'password',) # tell django which fields to include

    def create(self, validated_data):
        user = User.objects.create(
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            email=validated_data['email'],
            username=validated_data['username'],
            password= make_password(validated_data['password'])
        )
        user.save()
        return user
    
    def update(self, instance, validated_data):
        user = User.objects.get(email=validated_data["email"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user