from django.contrib.auth.models import User
from rest_framework import serializers

from REST_User.users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password')

    class Meta:
        model = Profile
        fields = ['id', 'username', 'password', 'bio']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user.set_password(user_data['password'])
        user.save()
        return Profile.objects.create(user=user, **validated_data)
