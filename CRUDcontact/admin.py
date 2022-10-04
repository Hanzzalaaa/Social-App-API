from django.contrib import admin
from .models import CRUD,Post,PostComment,PostLike

# Register your models here.
@admin.register(CRUD)
class AdminCRUD(admin.ModelAdmin):
    list_display = ['owner','id','country_code','first_name','last_name','phone_number','contact_picture','is_favourite']


@admin.register(Post)
class PostCRUD(admin.ModelAdmin):
    list_display = ['id','post']


@admin.register(PostLike)
class PostLikeCRUD(admin.ModelAdmin):
    list_display = ['id','postlike','userlike']



@admin.register(PostComment)
class PostCommentCRUD(admin.ModelAdmin):
    list_display = ['id','postcomment','usercomment']


