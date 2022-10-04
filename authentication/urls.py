from django.urls import path
from .views import RegisterView,LoginView,VerifyEmail


urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('email-verify',VerifyEmail.as_view(),name='email-verify'),
]