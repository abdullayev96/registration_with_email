from rest_framework import serializers
from .models import *



class RegisterSerializer(serializers.ModelSerializer):
      password = serializers.CharField(max_length=50, min_length=6, write_only=True)

      class Meta:
           model = User
           fields  = ['email', 'username','password']


      def validate(self, attrs):
          email  = attrs.get("email", "")
          username = attrs.get("username", "")

          if not username.isalnum():
             raise serializers.ValidationError(self.default_error_messages)
          return attrs

      def create(self, validated_data):
          return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']
