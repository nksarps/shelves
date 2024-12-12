from .models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=50, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'created_at']

        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=50, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(username=email, password=password)

        if not user:
            serializers.ValidationError('Invalid credentials', code='authentication')

        attrs['user'] = user
        return attrs

    def generate_tokens(self, attrs):
        user = attrs['user']

        refresh = RefreshToken.for_user(user)

        tokens = {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

        return tokens

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields = ['id', 'first_name', 'last_name', 'username', 'email', 'created_at']