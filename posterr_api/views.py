from rest_framework import viewsets


from posterr_api import serializers
from posterr_api import models


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    queryset = models.User.objects.all()
