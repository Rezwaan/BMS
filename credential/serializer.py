__author__ = 'Amad'

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserDetails,sendFriends



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name','last_name','username',  'password','email')


class friendEmailSerilizer(serializers.ModelSerializer):

    class Meta:
        model = sendFriends
        fields =('email','sharedlink')

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','email', 'password')


class UserLoginIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username')

class UserDetailsSerializer(serializers.Serializer):

    id = serializers.IntegerField(label='ID', read_only=True)
    user_id = serializers.IntegerField()
    Mobile = serializers.CharField()
    email = serializers.CharField()
    newsLetter=serializers.BooleanField()
    class Meta:
      model = UserDetails
      fields = {
      'id',
      'Mobile',
      'email',
      'newsLetter',
      }
    def create(self, validated_data):
      return UserDetails.objects.create(**validated_data)