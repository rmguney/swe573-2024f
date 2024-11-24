from django.test import TestCase
from django.db import IntegrityError
from django.utils import timezone
from threef.models import Thread, Comment

class ThreadModelTest(TestCase):

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

    def test_thread_creation(self):
        """Test thread creation with required fields"""
        self.assertEqual(self.thread.title, "Test Thread")
        self.assertEqual(self.thread.description, "Test description")
        self.assertEqual(self.thread.voteCount, 10)

    def test_thread_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.thread), "Test Thread")

    def test_thread_optional_fields(self):
        """Test optional fields with null or empty values"""
        thread_with_optional_fields = Thread.objects.create(
            title="Thread with optional fields",
            description="Another description",
            tags=["Q16338"],
            imageSrc="http://example.com/image.jpg",
            postedBy="another_user"
        )
        self.assertIsNone(thread_with_optional_fields.material)
        self.assertIsNone(thread_with_optional_fields.size)

    def test_thread_empty_tags(self):
        """Test empty tags field"""
        thread_empty_tags = Thread.objects.create(
            title="Thread with empty tags",
            description="Some description",
            tags=[],
            imageSrc="http://example.com/image.jpg",
            postedBy="test_user"
        )
        self.assertEqual(thread_empty_tags.tags, [])

class CommentModelTest(TestCase):

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

    def test_comment_creation(self):
        """Test that comment is created correctly"""
        self.assertEqual(self.comment.comment, "Test comment")
        self.assertEqual(self.comment.voteCountComment, 5)
        self.assertEqual(self.comment.commentator, "commenter1")

    def test_comment_str(self):
        """Test the __str__ method for comments"""
        self.assertEqual(str(self.comment), f"Comment by commenter1 on {self.thread.title}")

    def test_comment_no_thread(self):
        """Test if comment without thread raises an error"""
        with self.assertRaises(IntegrityError):
            Comment.objects.create(
                comment="Test comment without thread",
                voteCountComment=0,
                commentator="commenter2",
                selected=False
            )
