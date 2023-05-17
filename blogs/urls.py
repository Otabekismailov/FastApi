from django.urls import path

from blogs.views import PostListApiView, PostDetailApiView, LikeApiView, AddCommentAPI

urlpatterns = [
    path('post/', PostListApiView.as_view(), name='post-list'),
    path('post/<slug:slug>', PostDetailApiView.as_view(), name='post-detail'),
    path('like/<slug:slug>', LikeApiView.as_view(), name='like-list'),
    path('comment/<slug:slug>', AddCommentAPI.as_view(), name='comment-add'),
]
