from django.urls import path
from .views import HelloWorldAPIView

urlpatterns = [
    path('numbers/', HelloWorldAPIView.as_view()),
]
