
# from django.contrib.auth.models import User
from Friend_Request.models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length =100 , min_length =6 , write_only= True)
    email = serializers.EmailField(max_length =200 , min_length =4 )
    first_name =serializers.CharField(max_length =100 , min_length =2)
    last_name =serializers.CharField(max_length =100 , min_length =2)
    

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','password']


    def validate(self,attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email',('Email is already in use')})
        return super().validate(attrs)


    def create(self,validated_data):
        user =User.objects.create_user(**validated_data)
        user.is_active = False
        user.save()
        return user

# class loginSerializer(serializers.ModelSerializer):
#         password = serializers.CharField(max_length =100 , min_length =6 , write_only= True)
#         username =serializers.CharField(max_length =100 , min_length =2)


