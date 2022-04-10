from rest_framework import viewsets
from rest_framework import filters
from posterr_api import serializers
from posterr_api import models


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'username',)
