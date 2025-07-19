from django.db import models
from merchant.models import Merchant

class Client(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='clients', null=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    job = models.CharField(max_length=100)

    def __str__(self):
         return f"{self.firstName} {self.lastName}"