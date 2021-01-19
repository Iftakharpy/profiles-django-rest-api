import json
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = HelloSerializer
    
    def list(self, request):
        """Return a list with even number from 1 to 99. And a "Hello" message."""
        response_list = [x for x in range(1,99) if x%2==0]
        return Response({'messge': "Hello World!", 'even_numbers': response_list})

    def create(self, request):
        """Create a hello message."""
        serialized_data = self.serializer_class(data=request.data)

        if serialized_data.is_valid():
            name = serialized_data.validated_data.get('name')
            message = f"Hello, {name}!"
            return Response({'message': message, 'method': request.method})
        return Response(
            serialized_data.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by it's ID."""
        return Response({'http_method': "GET", 'method': request.method})
    
    def update(self, request, pk=None):
        """Handle updating an object by it's ID."""
        return Response({'http_method': 'PUT', 'method': request.method})

    def partial_update(self, request, pk=None):
        """Handle updating the provided fields with only the provided fields by it's ID."""
        return Response({'http_method': 'PATCH', 'method': request.method})
    
    def destroy(self, request, pk=None):
        """Handle deleting an object by it's ID."""
        return Response({'http_method': "DELETE", 'method': request.method})


def json_response(request, count):
    # print(request.user)
    
    a = [x for x in range(count) if x%10==0]
    resp = {'logged_in': request.user.is_authenticated, 'status': 'success', 'nums': a}
    if request.user.is_authenticated:
        return HttpResponse(json.dumps(resp))
    return HttpResponse('Error 404: Not found.')
