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
        data = {
            'description': 'Thread with no title',
            'tags': ["Q16338", "Q204370"],
            'imageSrc': "http://example.com/image.jpg",
            'postedBy': "test_user",
            'voteCount': 0
        }
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

class CommentViewSetTest(APITestCase):
    def setUp(self):
        """Create a thread and comment for testing"""
        self.thread = Thread.objects.create(
            title="Test Thread",
            description="Test description",
            tags=["Q16338", "Q204370"],
            imageSrc="http://example.com/image.jpg",
            postedBy="test_user",
            voteCount=10
        )
        self.comment = Comment.objects.create(
            thread=self.thread,
            comment="Test comment",
            voteCountComment=5,
            commentator="commenter1"
        )
        self.url = reverse('comment-list')

    def test_comment_create(self):
        """Test creating a comment"""
        data = {
            'thread': self.thread.id,
            'comment': 'New comment',
            'voteCountComment': 0,
            'commentator': 'commenter2'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['comment'], 'New comment')

    def test_comment_create_missing_comment(self):
        """Test creating a comment with missing comment field (should fail)"""
        data = {
            'thread': self.thread.id,
            'voteCountComment': 0,
            'commentator': 'commenter2'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_comment_list(self):
        """Test retrieving the list of comments"""
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_comment_detail(self):
        """Test retrieving the details of a comment"""
        url = reverse('comment-detail', kwargs={'pk': self.comment.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comment'], "Test comment")

    def test_comment_update(self):
        """Test updating a comment"""
        url = reverse('comment-detail', kwargs={'pk': self.comment.id})
        data = {'comment': 'Updated comment'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comment'], 'Updated comment')

    def test_comment_delete(self):
        """Test deleting a comment"""
        url = reverse('comment-detail', kwargs={'pk': self.comment.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_comment_not_found(self):
        """Test accessing a non-existing comment"""
        url = reverse('comment-detail', kwargs={'pk': 999999})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
