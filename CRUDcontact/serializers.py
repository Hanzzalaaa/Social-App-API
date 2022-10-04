from django.db import connection
from .models import CRUD,PostComment,Post,PostLike,User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class CRUDSerializer(ModelSerializer):
    class Meta:
        model = CRUD
        fields = ['owner','id','country_code','first_name','last_name','phone_number','contact_picture','is_favourite']



class PostLikeSerializer(ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id','postlike','userlike']

class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['id','postcomment','usercomment']



class PostSerializer(ModelSerializer):
    Like = PostLikeSerializer(many=True,read_only=True)
    Comment = PostCommentSerializer(many=True,read_only=True)


    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        # select_related for "to-one" relationships
        # queryset = queryset.prefetch_related('post')
        # prefetch_related for "to-many" relationships
        queryset = queryset.prefetch_related(
            'Like',
            'Comment')
        # queryset=queryset
        print(queryset)
        for i in queryset:
            print(i.Like.all())
            print(i.Comment.all())
        print('sql:',len(connection.queries))
        
        # # Prefetch for subsets of relationships
        # queryset = queryset.prefetch_related(
        #     Prefetch('unaffiliated_attendees', 
        #         queryset=Attendee.objects.filter(organization__isnull=True))
        #     )
        return queryset
    class Meta:
        model = Post
        fields = ['id','post','Like','Comment']
    



class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)






