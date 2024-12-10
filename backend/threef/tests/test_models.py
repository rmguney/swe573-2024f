from django.test import TestCase
from django.utils.timezone import now
from threef.models import Thread, Comment


class ThreadModelTestCase(TestCase):
    def setUp(self):
        # Create a sample thread for testing
        self.thread = Thread.objects.create(
            title="Sample Thread",
            description="This is a sample thread description.",
            tags=["Q16338", "Q204370"],
            labels=["Example Tag 1", "Example Tag 2"],
            imageSrc="http://example.com/image.jpg",
            postedBy="test_user",
            voteCount=10,
            material="Plastic",
            size="Medium",
            shape="Round",
            color="Blue",
            texture="Smooth",
            weight="Light",
            smell="Neutral",
            marking="None",
            functionality="Example functionality",
            period="Modern",
            location="Unknown",
            resolved=False
        )

    def test_thread_creation(self):
        """Test that a thread is created correctly."""
        self.assertEqual(self.thread.title, "Sample Thread")
        self.assertEqual(self.thread.description, "This is a sample thread description.")
        self.assertEqual(self.thread.tags, ["Q16338", "Q204370"])
        self.assertEqual(self.thread.labels, ["Example Tag 1", "Example Tag 2"])
        self.assertEqual(self.thread.imageSrc, "http://example.com/image.jpg")
        self.assertEqual(self.thread.postedBy, "test_user")
        self.assertEqual(self.thread.voteCount, 10)
        self.assertEqual(self.thread.material, "Plastic")
        self.assertFalse(self.thread.resolved)

    def test_thread_str_method(self):
        """Test the __str__ method of the Thread model."""
        self.assertEqual(str(self.thread), "Sample Thread")

    def test_thread_update(self):
        """Test updating a thread."""
        self.thread.voteCount += 1
        self.thread.resolved = True
        self.thread.save()

        updated_thread = Thread.objects.get(id=self.thread.id)
        self.assertEqual(updated_thread.voteCount, 11)
        self.assertTrue(updated_thread.resolved)


class CommentModelTestCase(TestCase):
    def setUp(self):
        # Create a sample thread
        self.thread = Thread.objects.create(
            title="Sample Thread",
            description="This is a sample thread description.",
            tags=["Q16338"],
            labels=["Example Tag"],
            imageSrc="http://example.com/image.jpg",
            postedBy="test_user",
        )

        # Create a sample comment for testing
        self.comment = Comment.objects.create(
            thread=self.thread,
            comment="This is a sample comment.",
            voteCountComment=5,
            commentator="test_commentator",
            selected=False,
        )

    def test_comment_creation(self):
        """Test that a comment is created correctly."""
        self.assertEqual(self.comment.comment, "This is a sample comment.")
        self.assertEqual(self.comment.voteCountComment, 5)
        self.assertEqual(self.comment.commentator, "test_commentator")
        self.assertEqual(self.comment.thread, self.thread)
        self.assertFalse(self.comment.selected)

    def test_comment_str_method(self):
        """Test the __str__ method of the Comment model."""
        expected_str = f"Comment by test_commentator on {self.thread.title}"
        self.assertEqual(str(self.comment), expected_str)

    def test_comment_update(self):
        """Test updating a comment."""
        self.comment.voteCountComment += 2
        self.comment.selected = True
        self.comment.save()

        updated_comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(updated_comment.voteCountComment, 7)
        self.assertTrue(updated_comment.selected)

    def test_comment_deletion(self):
        """Test deleting a comment."""
        comment_id = self.comment.id
        self.comment.delete()
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(id=comment_id)

    def test_cascade_deletion(self):
        """Test that deleting a thread cascades to delete its comments."""
        thread_id = self.thread.id
        self.thread.delete()
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(thread_id=thread_id)
