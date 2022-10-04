from email.policy import default
from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# from django.utils.translation import ugettext_lazy as _
# Create your models here.

# from django.contrib.auth.models import User

class User(AbstractUser):
    friends = models.ManyToManyField("User", blank=True)
    is_verified = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE,)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.to_user