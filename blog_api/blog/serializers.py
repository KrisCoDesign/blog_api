from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={
        'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'password did not match.'})
        return attrs
    
    def create(self, validation_data):
        user = User.objects.create_user(
            username=validation_data['username'],
            email=validation_data['email'],
            password=validation_data['password']
        )
        return user