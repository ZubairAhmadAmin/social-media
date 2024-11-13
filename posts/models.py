from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=512)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'Post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
        
    def __str__(self):
        return self.title
        
        
class PostFile(models.Model):
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE, related_name='postfile')
    title = models.CharField(max_length=50)
    file = models.FileField()
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
        
    class Meta:
        db_table = 'Post-File'
        verbose_name = 'Post-File'
        verbose_name_plural = 'Post-Files'
        
        
    def __str__(self):
        return self.title
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    is_approved = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)     


    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'


class Like(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='likes')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = 'like'
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'