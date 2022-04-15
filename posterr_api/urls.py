from django.urls import path, include

from rest_framework.routers import DefaultRouter

from posterr_api import views

# This is useful for the url in the automated tests
app_name = 'api'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('userprofile', views.UserViewSet, basename='user')
router.register('homepage', views.HomepageViewSet, basename='homepage')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
