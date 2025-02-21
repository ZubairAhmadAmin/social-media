from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Countries'
        verbose_name = 'Country'
        
    def __str__(self):
        return self.name
        

class Profile(models.Model):
    
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, upload_to='profile_avatars')
    
    def __str__(self) -> str:
        return f'{self.user} - {self.phone_number}'
    

 
class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_TYPE_CHOICES = (
        (DEVICE_WEB, 'web'),
        (DEVICE_IOS, 'iso'),
        (DEVICE_ANDROID, 'android'),
        (DEVICE_PC, 'pc')
    )
    
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='devices', on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device UUID', null=True)
    last_login = models.DateTimeField('last login date', null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES, default=DEVICE_WEB)
    device_os = models.CharField('device os', max_length=20, blank=True)
    device_model = models.CharField('device model', max_length=50, blank=True)
    app_version = models.CharField('app version', max_length=20, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table = 'user_device'
        verbose_name = _('device')
        verbose_name_plural = _('devices')
