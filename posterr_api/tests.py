from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from django.test import TestCase
from .models import User, Post
from .serializers import UserSerializer, PostSerializer

client = APIClient()


# Sorry for these simple tests, I am running out of time, so I am
# keeping it simple to respect the deadline =).
class UserViewSetTests(TestCase):
    """
    The list of users should be available properly.
    """

    def setUp(self):
        self.user_attributes = {
            "name": "This is a test user",
            "email": "test_user@test.com",
            "username": "testUser",
            "password": "123",
            "created_at": "2022-04-14T03:18:03.497248Z"
        }

    def test_empty_user_list(self):
        response = self.client.get(reverse('api:user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.context, None)

    def test_user_list_after_user_insertion(self):
        self.user = User.objects.create(**self.user_attributes)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        response = self.client.get(reverse('api:user-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertQuerysetEqual(response.data, serializer.data)


class PostViewSetTests(TestCase):
    """
    The list of posts should be available properly.
    """

    def setUp(self):
        self.user_attributes = {
            "name": "This is a test user",
            "email": "test_user@test.com",
            "username": "testUser",
            "password": "123",
            "created_at": "2022-04-14T03:18:03.497248Z"
        }
        self.post_attributes = {
            "user": User.objects.create(**self.user_attributes),
            "text": "Test post"
        }

    def test_empty_post_list(self):
        response = self.client.get('/api/homepage/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.context, None)

    def test_post_list_after_post_insertion(self):
        self.post = Post.objects.create(**self.post_attributes)
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        response = self.client.get('/api/homepage/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertQuerysetEqual(response.data['results'], serializer.data)
