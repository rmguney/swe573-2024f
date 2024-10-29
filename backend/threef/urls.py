from django.urls import path
from threef.views import (
    ThreadViewSet, 
    CommentViewSet, 
    RegisterationAPIView, 
    LoginAPIView, 
)
from . import views
from rest_framework.routers import DefaultRouter

# Initialize the router
router = DefaultRouter()
router.register(r'thread', ThreadViewSet)
router.register(r'comment', CommentViewSet)

# Define the URL patterns
urlpatterns = router.urls

# Add additional paths for custom views
urlpatterns += [
    path('register/', RegisterationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('upload/', views.upload_file_view, name='upload_file'),  # Add this line for the upload view

]
