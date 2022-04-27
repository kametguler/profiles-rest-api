from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet,
                basename='hello-viewset')
router.register('profile', UserProfileViewSet, basename='User-Profile')

urlpatterns = [
    path("hello/", HelloApiView.as_view(), name="hello"),
    path('', include(router.urls))
]
