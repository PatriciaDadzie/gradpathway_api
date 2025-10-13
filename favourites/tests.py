from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from catalog.models import Programme, University


# Create your tests here.

User = get_user_model()

class FavouriteTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass123")
        self.client.force_authenticate(user=self.user)
        uni = University.objects.create(name="Test University", country="USA")
        self.programme = Programme.objects.create(
            university=uni,
            title="MSc Computer Science",
            discipline="Computer Science",
            duration_months=24,
            tuition=20000,
            currency="USD",
            min_gpa=3.0,
            mode="on-campus"
        )

    def test_add_favourite(self):
        response = self.client.post(reverse("favourite-list-create"), {"programme": self.programme.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_favourites(self):
        self.client.post(reverse("favourite-list-create"), {"programme": self.programme.id})
        response = self.client.get(reverse("favourite-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
