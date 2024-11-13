from django.contrib import admin
from django.http import HttpRequest

from .models import Friendship


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ['request_from', 'request_to', 'is_accepted', 'created_time']
    actions = False
    

    # def has_add_permission(self, request: HttpRequest):
    #     return False
    
    
    # def has_delete_permission(self, request: HttpRequest):
    #     return False