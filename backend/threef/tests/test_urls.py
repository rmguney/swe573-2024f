# tests/test_urls.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from threef.views import (
    ThreadViewSet,
    CommentViewSet,
    RegisterationAPIView,
    LoginAPIView,
    voteCount,
    voteCountComment,
)
from rest_framework import status
from threef import views  # Add this import statement

class TestUrls(SimpleTestCase):

    def test_thread_url(self):
        """Test if the 'thread' URL correctly resolves to the ThreadViewSet."""
        url = reverse('thread-list')  # Using the name of the route registered by DRF
        self.assertEqual(resolve(url).func.view_class, ThreadViewSet)

    def test_comment_url(self):
        """Test if the 'comment' URL correctly resolves to the CommentViewSet."""
        url = reverse('comment-list')
        self.assertEqual(resolve(url).func.view_class, CommentViewSet)

    def test_register_url(self):
        """Test if the 'register' URL correctly resolves to the RegisterationAPIView."""
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterationAPIView)

    def test_login_url(self):
        """Test if the 'login' URL correctly resolves to the LoginAPIView."""
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginAPIView)

    def test_upload_url(self):
        """Test if the 'upload' URL correctly resolves to the upload_file_view."""
        url = reverse('upload_file')
        self.assertEqual(resolve(url).func, views.upload_file_view)

    def test_voteCount_url(self):
        """Test if the 'voteCount' URL correctly resolves to the voteCount view."""
        url = reverse('voteCount')
        self.assertEqual(resolve(url).func, voteCount)

    def test_voteCountComment_url(self):
        """Test if the 'voteCountComment' URL correctly resolves to the voteCountComment view."""
        url = reverse('voteCountComment')
        self.assertEqual(resolve(url).func, voteCountComment)
