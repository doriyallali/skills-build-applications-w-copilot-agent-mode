from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class ApiRootTests(APITestCase):
    def test_api_root_returns_expected_endpoints(self):
        response = self.client.get(reverse('api-root'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)


class UserEndpointTests(APITestCase):
    def test_create_user(self):
        payload = {
            'username': 'tester',
            'email': 'tester@example.com',
            'first_name': 'Test',
            'last_name': 'User',
        }

        response = self.client.post(reverse('users-list'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
