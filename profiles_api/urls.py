from django.urls import path, include
from .views import HelloWorldAPIView, HelloViewSet, json_response
from rest_framework.routers import DefaultRouter

#retister the HelloViewSet
router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('json/<int:count>/', json_response),
    path('hello-view/', HelloWorldAPIView.as_view()),
    path('', include(router.urls))
]
