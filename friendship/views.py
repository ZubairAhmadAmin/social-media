from django.contrib .auth import get_user_model

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Friendship

from .serializer import UserListSerializer


User = get_user_model()


class UserListView(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request):
        users = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
        
        

class  RequestView(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def post(self, request):
        user_id = request.data.get('user')
         
        try: 
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
        Friendship.objects.get_or_create(request_from=request.user, request_to=user)
        
        return Response({'detail': 'Request sent'}, status=status.HTTP_201_CREATED)
    
    
    
class RequestList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        friendship = Friendship.objects.all()
        users = [fr.request_from for fr in friendship]
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
        
            
            
            
class AcceptedView(APIView):
    # parser_classes = [IsAuthenticated]
    
    def post(self, request):
        user_id = request.data.get('user')
        
        try:
            user = User.objects.get(pk=user_id) 
            friendship = Friendship.objects.get(request_from=user, request_to=request.user, is_accepted=False)
        except (User.DoesNotExist, Friendship.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        friendship.is_accepted = True
        friendship.save()
        
        return Response({'detail': 'Connected'})   
             
             
             
             
             
             