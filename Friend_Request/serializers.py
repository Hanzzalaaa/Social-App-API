from rest_framework import serializers
from Friend_Request.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id','friends', 'from_user', 'to_user']