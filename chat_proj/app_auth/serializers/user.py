
from ..models import users
from rest_framework import serializers

class UserDetailSerializer(serializers.ModelSerializer):
    """
    User detail serializer
    """
    class Meta:
        model = users
        fields = '__all__'