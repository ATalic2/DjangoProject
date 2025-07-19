from rest_framework import serializers
from .models import Client
from merchant.models import Merchant

class ClientSerializer(serializers.ModelSerializer):
    merchant = serializers.PrimaryKeyRelatedField(queryset=Merchant.objects.all())

    class Meta:
        model = Client
        fields = '__all__'