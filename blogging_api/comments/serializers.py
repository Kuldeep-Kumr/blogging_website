from rest_framework import serializers
from .models import Comment, Reply


class CommentSerializer(serializers.ModelSerializer):
    comment_desc = serializers.CharField(max_length=1000, required=True)

    class Meta:
        model = Comment
        fields = ('__all__')

    def create(self, validated_data):

        return Comment.objects.create(**validated_data)



class ReplySerializer(serializers.ModelSerializer):
    reply_desc = serializers.CharField(max_length=1000, required=True)

    class Meta:
        model = Reply
        fields = ('__all__')

    def create(self, validated_data):
        return Reply.objects.create(**validated_data)
