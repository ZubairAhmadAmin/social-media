from django.urls import path

from .views import UserListView, RequestView, RequestList, AcceptedView

urlpatterns = [
    path('users-list/', UserListView.as_view(), name='user-list'),
    path('request/', RequestView.as_view(), name='request'),
    path('request-list/', RequestList.as_view(), name='request-list'),
    path('accept/', AcceptedView.as_view(), name='accepted'),
    # path('friends/')
]