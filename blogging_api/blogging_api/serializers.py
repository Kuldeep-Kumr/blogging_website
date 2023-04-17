from rest_framework import serializers  
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer): 
    username = serializers.CharField(max_length=200, required=True)   
    password = serializers.CharField(max_length=200, required=True)  
    
    class Meta:  
        model = User
        fields = ['username','password'] 

    def create(self, validated_data):  
        """ 
        Create and return a new `Users` instance, given the validated data. 
        """ 
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user