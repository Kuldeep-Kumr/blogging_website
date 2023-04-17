from django.shortcuts import get_object_or_404
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Comment,Reply
from .serializers import CommentSerializer,ReplySerializer 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CommentView(APIView):  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):  
        result = Comment.objects.filter(blog_id=id)
        serializers = CommentSerializer(result,many=True)  
        return Response({'success': 'success', "Comments":serializers.data}, status=200)  

    def post(self, request,id):
        request.data['blog_id']=id
        serializer = CommentSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "Comments": serializer.data}, status=status.HTTP_200_OK)  
        return Response({"status": "error", "Comments": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)   
    
class ReplyView(APIView):  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id):  
        result = Reply.objects.filter(comment_id=id)
        serializers = ReplySerializer(result,many=True)  
        if id:  
            serializers = ReplySerializer(result,many=True)  
            return Response({'success': 'success', "Replys":serializers.data}, status=200)  
    
    def post(self, request,id):  
        request.data['comment_id']=id
        serializer = ReplySerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "Replys": serializer.data}, status=status.HTTP_200_OK)  
    
