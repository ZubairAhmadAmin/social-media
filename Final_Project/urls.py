from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

from accounts.views import RegisterView

from blog.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('api/', include('asset.urls')),
    
    
    
    path('api/register/', RegisterView.as_view()),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/', include('posts.urls')),
    
    path('api/friendship/', include('friendship.urls'))
]

from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static('/media', document_root=settings.MEDIA_ROOT)