from rest_framework import serializers
from .models import Order, OrderContactInfo

class OrderContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderContactInfo
        fields = '__all__' 

class OrderSerializer(serializers.ModelSerializer):
    contact_info = OrderContactInfoSerializer()

    class Meta:
        model = Order
        fields = '__all__'  