# authapp/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'name')
        extra_kwargs = {'password': {'write_only': True}, 'username': {'read_only': True}}

    def create(self, validated_data):
        name = validated_data.pop('name')
        user = User.objects.create_user(
            username=validated_data['email'],  # Setting the email as the username
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=name  # Storing name in first_name field
        )
        return user
