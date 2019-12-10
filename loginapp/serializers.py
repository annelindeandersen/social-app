from rest_framework import serializers
from loginapp.models import User

#loginap serialiser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # gets all fields from User models
        fields = '__all__'