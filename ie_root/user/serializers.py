from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'date_joined', 'is_staff', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['is_staff', 'date_joined']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
