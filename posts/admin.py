from django.contrib import admin
from .models import Post, PostFile, Comment, Like


class PostFileInlineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('title', 'file')
    extra = 0

class PostCommentInlineAdmin(admin.StackedInline):
    model = Comment
    fields = ('post', 'text', 'is_approved')
    extra = 0
    
class PostLikeInlineAdmin(admin.StackedInline):
    model = Like
    fields = ('post', 'is_liked')
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_active', 'create_time')
    inlines = (PostFileInlineAdmin, PostCommentInlineAdmin, PostLikeInlineAdmin)


# @admin.register(PostFile)
# class PostFileAdmin(admin.ModelAdmin):
#     psss