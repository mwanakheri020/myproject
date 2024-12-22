from rest_framework import serializers
from .models import*

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'customername', 'email', 'is_landlord', 'is_tenant']

class PropertySerializer(serializers.ModelSerializer):
    landlord = UserSerializer(read_only=True)  # Include landlord details in the response

    class Meta:
        model = Property
        fields = ['id', 'title', 'description', 'address', 'rent', 'landlord', 'available']



class PaymentSerializer(serializers.ModelSerializer):
    lease = LeaseSerializer(read_only=True)  # Include lease details in the response

    class Meta:
        model = Payment
        fields = ['id', 'lease', 'amount', 'payment_date', 'is_paid']
