from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_desc = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)