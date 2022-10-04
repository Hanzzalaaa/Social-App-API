# from django.contrib.auth.models import User
from Friend_Request.models import User
import jwt
from rest_framework import authentication , exceptions
from django.conf import settings


class JWTauthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        # print("request", request)
        auth_data = authentication.get_authorization_header(request)
        # print("auth_data", auth_data)


        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split(' ')
        print(token)
        print(settings.JWT_SECRET_KEY)
        # print(jwt.decode(token,settings.JWT_SECRET_KEY))
        try:
            payload = jwt.decode(token,settings.JWT_SECRET_KEY, algorithms=['HS256'])
            print("payload",payload)
            user=User.objects.get(username=payload['username'])
            return (user,token)

        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('your token is Invalid,Login Again')


        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('your token is Expired,Login Again')


      