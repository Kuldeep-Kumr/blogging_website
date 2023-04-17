from django.shortcuts import get_object_or_404
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer  
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AllBlogView(APIView):  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        result = Blog.objects.all()
        serializers = BlogSerializer(result,many=True) 
        return Response({'Status': 'Success', "Blogs":serializers.data}, status=200)
        
    def post(self, request): 
        request.data['username']=request.user.id
        serializer = BlogSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "Blogs": serializer.data}, status=status.HTTP_200_OK)  
        return Response({"status": "error", "Blogs": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 

 
class BlogView(APIView):  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):  
        result = Blog.objects.filter(blog_id=id)
        if len(result)>0:
            serializers = BlogSerializer(result[0]) 
            return Response({'success': 'success', "Blogs":serializers.data}, status=200)
        return Response({'success': 'success', "Blogs":"None"}, status=200)     
    
  
    def patch(self, request, id):  
        result = Blog.objects.get(blog_id=id)
        if str(result.username)==str(request.user.username):
            serializer = BlogSerializer(result, data = request.data, partial=True)  
            if serializer.is_valid():  
                serializer.save()  
                return Response({"Status": "Success", "Blogs": serializer.data},status=200)
            return Response({"Status": "Error", "Blogs": serializer.data},status=404) 
        elif len(request.data)==1 and 'likes' in request.data:
            serializer = BlogSerializer(result, data = request.data, partial=True)  
            if serializer.is_valid():  
                serializer.save()  
                return Response({"Status": "Success", "Blogs": serializer.data},status=200)
            return Response({"Status": "Error", "Blogs": serializer.data},status=404) 
        return Response({"Status": "Invalid user", "Blogs": []},status=403)
    
    def delete(self, request, id=None):  
        result = get_object_or_404(Blog, blog_id=id) 
        if str(result.username)==str(request.user.username):
            result.delete()  
            return Response({"status": "success", "data": "Record Deleted"})  
        return Response({"Status": "Invalid user", "data": "None"},status=403)
    