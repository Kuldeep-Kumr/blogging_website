from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from django.contrib.auth.models import User
from .serializers import UserSerializer  
from rest_framework.authtoken.models import Token

class UserRegisterView(APIView):  

    def get(self, request): 
        return Response({'status': 'Register','Token': 'None'}, status=200)  
  
    def post(self, request): 
        serializer = UserSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            user=User.objects.get(username=serializer.data['username'])
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"status": "success","token":str(token)}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
