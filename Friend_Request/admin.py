from django.contrib import admin

from Friend_Request.models import FriendRequest, User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ['id','username']

@admin.register(FriendRequest)
class FriendAdmin(admin.ModelAdmin):
    list_display = [
        "id", "from_user","to_user"
    ]