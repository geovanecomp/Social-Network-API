from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posterr_api import paginations
from posterr_api import serializers
from posterr_api import models
from posterr_api import permissions


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user profiles"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name', 'email', 'username',)
    ordering_fields = ['name', 'email']


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class PostViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user posts"""
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = models.Post.objects.all()


class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    """Show all posts sorted by latest and paginated in the feed as read only"""
    pagination_class = paginations.StandardResultsSetPagination
    serializer_class = serializers.PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('text',)
    queryset = models.Post.objects.order_by('created_at').reverse()
