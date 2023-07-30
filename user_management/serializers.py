# serializers.py
from rest_framework import serializers

from .models import UserInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'full_name', 'address_1', 'address_2', 'city', 'state', 'zip_num', 'username', 'password')
    
class FuelQuoteSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('gallons_requested', 'location')
    