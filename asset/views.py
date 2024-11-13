from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# from common.views import CustomPageNumberPagination
from .models import Category
from .serializers import CategorySerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000



# Create your views here.
class CategoryView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    permission_classes = (IsAuthenticated)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['name']
    ordering = ['-id'] 
    search_fields = ['id', 'name', 'description','created_at', 'updated_at']


    def get(self, request, pk=None):
        try:
            if pk:
                category = self.retrieve(request, pk).data
                return Response({'category': category}, status=status.HTTP_200_OK)
            
            category = self.list(request).data
            return Response({'category': category}, status=status.HTTP_200_OK)
        
        except Category.ObjectDoesNotExist:
            return Response({'error': 'Category not found.'},status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def post(self, request):
        try:
            category = self.create(request).data
            return Response({'category': category}, status=status.HTTP_201_CREATED)
        
        except ValidationError as e:
            return Response({'error': e.detail},status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, request, pk=None):
        try:
            category = self.update(request, pk, partial=True).data
            return Response({'category': category}, status=status.HTTP_202_ACCEPTED)
        
        except Category.ObjectDoesNotExist:
            return Response({'error': 'Category not found.'},status=status.HTTP_404_NOT_FOUND)
        
        except ValidationError as e:
            return Response({'error': e.detail},status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete(self, request, pk=None):
        try:
            self.destroy(request, pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Category.ObjectDoesNotExist:
            return Response({'error': 'Category not found.'},status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
