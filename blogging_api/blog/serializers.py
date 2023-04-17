from rest_framework import serializers  
from .models import Blog
  
class BlogSerializer(serializers.ModelSerializer):
    blog_desc = serializers.CharField(max_length=1000, required=True) 
    
    class Meta:  
        model = Blog
        fields = ('__all__')  

    def create(self, validated_data):  

        return Blog.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        instance.blog_desc = validated_data.get('blog_desc', instance.blog_desc)    
        instance.likes = validated_data.get('likes', instance.likes)  
        instance.save()  
        return instance