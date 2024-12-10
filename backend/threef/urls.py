from django.urls import path
from threef.views import (
    ThreadViewSet,
    CommentViewSet,
    RegisterationAPIView,
    LoginAPIView,
    add_reply,
    toggle_comment_selected
)
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'thread', ThreadViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('register/', RegisterationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('upload/', views.upload_file_view, name='upload_file'),
    path('threads/<int:thread_id>/updateResolved', views.update_resolved_status, name='update_resolved'),
    path('comments/<int:comment_id>/toggle-selected/', views.toggle_comment_selected, name='toggle_comment_selected'),
    path('comments/<int:comment_id>/add-reply/', add_reply, name='add-reply'),
]
