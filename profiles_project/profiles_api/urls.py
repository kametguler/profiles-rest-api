from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewSet, LoginViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet,
                basename='hello-viewset')
router.register('profile', UserProfileViewSet, basename='User-Profile')
router.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path("hello/", HelloApiView.as_view(), name="hello"),
    path('', include(router.urls))
]
