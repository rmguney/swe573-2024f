# tests/test_views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from threef.models import Thread, Comment
from django.contrib.auth.models import User

class ThreadViewSetTest(APITestCase):

    def setUp(self):
        """Create a thread for testing"""
        self.thread = Thread.objects.create(
            title="Test Thread",
            description="Test description",
            tags=["Q16338", "Q204370"],
            imageSrc="http://example.com/image.jpg",
            postedBy="test_user",
            voteCount=10
        )
        self.url = reverse('thread-list')  # Adjust this to your actual endpoint URL

    def test_thread_create(self):
        """Test creating a thread"""
        data = {
            'title': 'New Thread',
            'description': 'New thread description',
            'tags': ["Q16338", "Q204370"],
            'imageSrc': "http://example.com/image.jpg",
            'postedBy': "test_user",
            'voteCount': 0
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Thread')

    def test_thread_create_missing_title(self):
        """Test creating a thread with missing title (should fail)"""
        data = {'description': 'Thread with no title'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_thread_list(self):
        """Test retrieving the list of threads"""
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_thread_detail(self):
        """Test retrieving the details of a thread"""
        url = reverse('thread-detail', kwargs={'pk': self.thread.id})  # Adjust as per your URL config
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Thread")

    def test_thread_update(self):
        """Test updating a thread"""
        url = reverse('thread-detail', kwargs={'pk': self.thread.id})  # Adjust as per your URL config
        data = {'title': 'Updated Thread'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Thread')

    def test_thread_delete(self):
        """Test deleting a thread"""
        url = reverse('thread-detail', kwargs={'pk': self.thread.id})  # Adjust as per your URL config
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_thread_not_found(self):
        """Test accessing a non-existing thread"""
        url = reverse('thread-detail', kwargs={'pk': 999999})  # Non-existent thread ID
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
