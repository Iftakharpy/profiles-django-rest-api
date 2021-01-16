from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloWorldAPIView(APIView):
    """Hello world API View"""

    def get(self, request, format=None):
        """Returns a list of APIViews"""
        a_list_of_numbers = [x if x%7==0 else x/7 for x in range(200, 300)]

        print(request.user)

        return Response({'message': 'Hello World!', 'numbers': a_list_of_numbers})

