# from http.client import HTTPResponse
from django.shortcuts import HttpResponse
from .models import FriendRequest,User
from django.shortcuts import render
from rest_framework import decorators
from rest_framework.decorators import api_view
from rest_framework import viewsets
# from Friend_Request.serializers import UserSerializer
from authentication.serializers import UserSerializer
from django.conf import settings
# User = settings.AUTH_USER_MODEL
# Create your views here.

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




@api_view(['POST'])
def send_friend_request(request, UserID):
    from_user =request.user
    print(from_user)
    to_user = User.objects.get(id = UserID)
    print(to_user)
    Friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)

    if created:
        return HttpResponse('Friend Request Sent')



@api_view(['POST'])
def accept_friend_request(request, requestID):
    Friend_request = FriendRequest.objects.get(id = requestID)
    print("from_user",Friend_request.from_user)
    print("to_user",Friend_request.to_user)
    if Friend_request.to_user == request.user:
        Friend_request.to_user.friends.add(Friend_request.from_user)
        Friend_request.from_user.friends.add(Friend_request.to_user)
        Friend_request.delete()
        return HttpResponse('Friend Request Accepted / You Are Now Friends')
    else:
        return HttpResponse('Friend Request Rejected')



@api_view(['POST'])
def ignore_friend_request(request, requestID):
    Friend_request = FriendRequest.objects.get(id = requestID)
    print("from_user",Friend_request.from_user)
    print("to_user",Friend_request.to_user)
    if Friend_request.to_user == request.user:
        Friend_request.delete()
        return HttpResponse('Friend Request Deleted')
    else:
        return HttpResponse('Error')



@api_view(['POST'])
def revert_friend_request(request, requestID):
    Friend_request = FriendRequest.objects.get(id = requestID)
    print("from_user",Friend_request.from_user)
    print("to_user",Friend_request.to_user)
    if Friend_request.from_user == request.user:
        Friend_request.delete()
        return HttpResponse('Your Request Is Cancelled')
    else:
        return HttpResponse('Cancel Request Error')