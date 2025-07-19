from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from merchant.models import Merchant

class MerchantAPITest(APITestCase):

    def setUp(self):
        if not User.objects.filter(username="admin").exists():
            self.user = User.objects.create_user(username="admin", password="admin123")
        else:
            self.user = User.objects.get(username="admin")

        # Auth token for JWT
        response = self.client.post("/api/token/", {
            "username": "admin",
            "password": "admin123"
        })
        self.access_token = response.data["access"]
        self.auth_headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}

        self.merchant_payload = {"name": "MerchantX"}
        self.merchant_obj = Merchant.objects.create(name="InitialMerchant")

    def test_create_merchant(self):
        url = reverse('merchant-post')
        response = self.client.post(url, self.merchant_payload, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Merchant.objects.count(), 5)

    def test_get_merchant_list(self):
        url = reverse('merchant-list')
        response = self.client.get(url, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 3)

    def test_patch_merchant(self):
        url = reverse('merchant-patch')
        payload = {
            "id": self.merchant_obj.id,
            "name": "UpdatedMerchant"
        }
        response = self.client.patch(url, payload, format='json', **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "UpdatedMerchant")

    def test_delete_merchant(self):
        url = reverse('merchant-delete', args=[self.merchant_obj.id])
        response = self.client.delete(url, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Merchant.objects.count(), 3)
