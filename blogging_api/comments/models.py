from django.db import models
from blog.models import Blog

# Create your models here.
class Comment(models.Model):
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment_id = models.AutoField(primary_key=True)
    comment_desc = models.CharField(max_length=1000)

class Reply(models.Model):
    comment_id = models.ForeignKey(Comment,on_delete=models.CASCADE)
    reply_id = models.AutoField(primary_key=True)
    reply_desc = models.CharField(max_length=1000)