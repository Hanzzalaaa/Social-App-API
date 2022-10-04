from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated   
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , RetrieveAPIView
from .models import CRUD,Post,PostLike,PostComment,User
from .serializers import CRUDSerializer,PostSerializer,PostLikeSerializer,PostCommentSerializer,ChangePasswordSerializer
from rest_framework import permissions,viewsets
from rest_framework.response import Response
from django.db import connection
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
# Create your views here.

class CRUDviews(ListCreateAPIView):

    serializer_class = CRUDSerializer
    permissions_classes = (permissions.IsAuthenticated,)


    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


    def get_queryset(self):
        return CRUD.objects.filter(owner=self.request.user)


class CRUDdetails(RetrieveUpdateDestroyAPIView):
    
    serializer_class = CRUDSerializer
    permissions_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"


    def get_queryset(self):
        return CRUD.objects.filter(owner=self.request.user)


class Owner(RetrieveAPIView):
    serializer_class = CRUDSerializer
    lookup_field = "owner"
       
    def get(request,owner):
        query_set= CRUD.objects.filter(owner=owner).order_by("-id")
        a = CRUDSerializer(query_set,many = True)
        return Response(a.data)

    # return CRUD.objects.filter(owner=self.request.user)





class PostViewSet(viewsets.ModelViewSet):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset = Post.objects.all()
        # Set up eager loading to avoid N+1 selects
        queryset = self.get_serializer_class().setup_eager_loading(queryset)  
        return queryset
    # print('SQL Quries :',queryset.query)

    # print('Return:',connection.queries)
    # print('No Of Queries Student:',len(connection.queries))



class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer



class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer



@api_view(['GET', 'POST'])
def home(request):
    student_data = Post.objects.all()
    print(type(student_data))
    data=PostSerializer(student_data,many=True).data
    print(type(data))
    for i in student_data:
        print(i.post)
    print('Return:',connection.queries)
    print('No Of Queries Student:',len(connection.queries))
    return Response({"data":data})
    # return render(request, 'NewQuerySets/home.html',{'students':student_data})






class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            # self.object.check_password(serializer.data.get("confirm_password"))
            if serializer.data.get("confirm_password") == serializer.data.get("new_password"):
                self.object.set_password(serializer.data.get("new_password"))

                
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)
            return Response({"New_Password is not same as Confirm_Password"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


