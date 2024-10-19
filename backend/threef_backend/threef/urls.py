from django.urls import path
from threef.views import ThreadListAPIView, CommentListAPIView, ThreadDetailAPIView, CommentDetailAPIView

urlpatterns = [
    path('thread/', ThreadListAPIView.as_view(), name='thread_list'),
    path('comment/', CommentListAPIView.as_view(), name='comment_list'),
    path('thread/<int:pk>/', ThreadDetailAPIView.as_view(), name='thread_detail'),
    path('comment/<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail'),
]