from django.urls import path
from threef.views import (
    ThreadViewSet,
    CommentViewSet,
    RegisterationAPIView,
    LoginAPIView,
    voteCount,
    voteCountComment,
    search,  # Import the search view
    get_user,  # Import the get_user view
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
    path('voteCount/', views.voteCount, name='voteCount'),  # Dedicated thread voting endpoint
    path('voteCountComment/', views.voteCountComment, name='voteCountComment'),  # Dedicated comment voting endpoint
    path('search/', search, name='search'),
    path('user/<int:id>/', get_user, name='get_user'),  # User details endpoint
]
