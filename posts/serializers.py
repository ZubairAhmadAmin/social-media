from rest_framework import serializers

from .models import Post, PostFile, Comment, Like



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user_id', 'title', 'caption', 'is_active', 'is_public')
        extra_kwargs = {
            'user': {'read_only':True}
            
        }
        
        


class PostFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFile
        fields = ('title', 'file')
        extra_kwargs = {
            'post': {'read_only':True}
        }



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'text')
        extra_kwargs = {
            'post': {'read_only':True},
            'user': {'read_only':True}
        }
        
        
        
class LikeSerializer(serializers.ModelSerializer):
    model = Like
    fields = ('post', 'user', 'is_liked')
    extra_kwargs = {
        'post': {'read_only':True},
        'user': {'read_only':True},
        'is_liked': {'required':False}
    }