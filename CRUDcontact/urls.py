from django.urls import path,include
from django.urls import re_path as url

from .views import CRUDviews,CRUDdetails,Owner,PostViewSet,PostLikeViewSet,PostCommentViewSet,home,ChangePasswordView
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'PostViewSet', PostViewSet, basename='PostViewSet')
router.register(r'PostLikeViewSet', PostLikeViewSet, basename='PostLikeViewSet')
router.register(r'PostCommentViewSet', PostCommentViewSet, basename='PostCommentViewSet')

urlpatterns = [
    path('',CRUDviews.as_view()),
    path('<int:id>',CRUDdetails.as_view()),
    path('<int:owner>',Owner.as_view()),
    url(r'^api/', include(router.urls)),
    path('home/',home),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),



]