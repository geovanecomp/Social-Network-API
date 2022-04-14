from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class DoesNotAllowPostUpdate(permissions.BasePermission):
    """Does not let users to update any post"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit posts"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return False
