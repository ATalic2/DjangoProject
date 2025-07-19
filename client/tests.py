# tests/test_clients.py (you can organize by app or feature)
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from client.models import Client
from merchant.models import Merchant

class ClientAPITest(APITestCase):

    def setUp(self):
        if not User.objects.filter(username="admin").exists():
            self.user = User.objects.create_user(username="admin", password="admin123")
        else:
            self.user = User.objects.get(username="admin")
        self.merchant = Merchant.objects.create(name="TestMerchant")
        self.client_payload = {
            "firstName": "John",
            "lastName": "Doe",
            "job": "Engineer",
            "merchant": self.merchant.id 
        }

        self.client_model_data = {
            "firstName": "John",
            "lastName": "Doe",
            "job": "Engineer",
            "merchant": self.merchant
        }
        response = self.client.post("/api/token/", {
            "username": "admin",
            "password": "admin123"
        })
        self.access_token = response.data["access"]
        self.auth_headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}

    def test_create_client(self):
        url = reverse('client-post')
        response = self.client.post(url, self.client_payload, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 4)

    def test_get_clients_list(self):
        Client.objects.create(**self.client_model_data)
        url = reverse('client-list')
        response = self.client.get(url, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 4)

    def test_patch_client(self):
        client_obj = Client.objects.create(**self.client_model_data)
        patch_url = reverse('client-patch')
        updated_data = {"id": client_obj.id, "firstName": "Updated"}
        response = self.client.patch(patch_url, updated_data, format="json", **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["firstName"], "Updated")
