from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet, RegisterView, ProfileView, ProfileViewSet, AuthorViewSet, BookViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import debug_toolbar


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="profile"),

]