from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30,unique=True)
    description = models.TextField()
    #some comme
    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=255)
    last_updated = models.DateField(auto_now=True)
    starter = models.ForeignKey(User,related_name='topic',on_delete = models.DO_NOTHING)
    board = models.ForeignKey(Board, related_name='topic',on_delete = models.DO_NOTHING)

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts',on_delete = models.DO_NOTHING)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete = models.DO_NOTHING)