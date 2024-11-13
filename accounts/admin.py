from django.contrib import admin
# from django.contrib.auth.models import User

from .models import Country, Device, Profile


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     model = User
#     list_display = ('id')

admin.site.register(Country)
admin.site.register(Device)
admin.site.register(Profile)
