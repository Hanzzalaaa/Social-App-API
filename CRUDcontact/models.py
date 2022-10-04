from email.policy import default
from django.db import models
from Friend_Request.models import User
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

# Create your models here.

class CRUD(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    contact_picture = models.URLField(null=True)
    is_favourite = models.BooleanField(default=True)


class Post(models.Model):
    post = models.ForeignKey(User,on_delete = models.CASCADE,related_name='Post')
    image = models.TextField(default='Bio')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)


class PostLike(models.Model):
    postlike = models.ForeignKey(Post,on_delete = models.CASCADE ,related_name='Like')
    userlike = models.ForeignKey(User,on_delete = models.CASCADE ,related_name='userlike')



class PostComment(models.Model):
    postcomment = models.ForeignKey(Post,on_delete = models.CASCADE,related_name='Comment')
    usercomment = models.ForeignKey(User,on_delete = models.CASCADE ,related_name='usercomment')



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "abdullahakhlaq14@gmail.com",
        # to:
        [reset_password_token.user.email]
    )