from rest_framework import serializers

from posterr_api import models


class UserSerializer(serializers.ModelSerializer):
    """Serializes a user object"""

    class Meta:
        model = models.User
        fields = ('id', 'name', 'email', 'username', 'password', 'followers', 'created_at')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.User(
            name=validated_data['name'],
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        # M2M relationship requires having a user instance saved first.
        followers = validated_data['followers']
        user.followers.add(*followers)
        return user

    def update(self, instance, validated_data):
        """Update a user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class PostSerializer(serializers.ModelSerializer):
    """Serializes a post object"""

    class Meta:
        model = models.Post
        fields = ('id', 'user', 'another_user_post', 'text', 'created_at')
