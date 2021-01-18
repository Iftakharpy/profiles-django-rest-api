from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer

# Create your views here.
class HelloWorldAPIView(APIView):
    """Hello world API View"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIViews"""
        numbers = [x for x in range(10)]

        return Response({'message': 'Hello World!', 'numbers': numbers})
    
    def post(self, request):
        """Create a hello message with our name"""
        serialized_data = self.serializer_class(data=request.data)
        
        if serialized_data.is_valid():
            name = serialized_data.validated_data.get('name')
            message = f"Hello, {name}!"
            return Response({'message': message})
        return Response(
            serialized_data.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def put(self, request, pk=None):
        """Update an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Update the fields provided in the request"""
        return Response({"method": 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})