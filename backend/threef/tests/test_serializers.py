from django.test import TestCase
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from threef.models import Thread, Comment
from threef.serializers import CommentSerializer, ThreadSerializer, RegisterationSerializer


class CommentSerializerTestCase(TestCase):
    def setUp(self):
        self.thread = Thread.objects.create(
            title="Sample Thread",
            description="This is a sample thread description",
            tags="sample,thread",
            labels="sample,thread",
            postedBy="test_user",
            imageSrc="http://example.com/image.jpg"
        )
        self.comment_data = {
            "thread": self.thread.id,
            "comment": "This is a test comment",
            "voteCountComment": 5,
            "commentator": "comment_user",
            "postedDateComment": "2024-01-01T12:00:00Z",
            "selected": False
        }
        self.serializer = CommentSerializer(data=self.comment_data)

    def test_valid_comment_serializer(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data["comment"], self.comment_data["comment"])

    def test_invalid_comment_serializer(self):
        invalid_data = self.comment_data.copy()
        invalid_data["thread"] = None  # thread is required
        serializer = CommentSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("thread", serializer.errors)


class ThreadSerializerTestCase(TestCase):
    def setUp(self):
        self.thread_data = {
            "title": "Sample Thread",
            "description": "This is a sample thread description",
            "tags": "sample,thread",
            "labels": "sample,thread",
            "postedBy": "test_user",
            "imageSrc": "http://example.com/image.jpg",
            "material": "plastic",
            "size": "medium",
            "shape": "round",
            "color": "blue",
            "texture": "smooth",
            "weight": "light",
            "smell": "none",
            "marking": "none",
            "functionality": "example",
            "period": "modern",
            "location": "unknown",
            "resolved": False
        }
        self.thread = Thread.objects.create(**self.thread_data)
        self.comment = Comment.objects.create(
            thread=self.thread,
            comment="This is a test comment",
            voteCountComment=3,
            commentator="comment_user"
        )
        self.serializer = ThreadSerializer(instance=self.thread)

    def test_thread_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {
            "id", "title", "description", "tags", "labels", "imageSrc",
            "postedBy", "postedDate", "voteCount", "comments", "material",
            "size", "shape", "color", "texture", "weight", "smell",
            "marking", "functionality", "period", "location", "resolved"
        })

    def test_thread_serializer_includes_comments(self):
        data = self.serializer.data
        self.assertIn("comments", data)
        self.assertEqual(len(data["comments"]), 1)
        self.assertEqual(data["comments"][0]["comment"], "This is a test comment")


class RegisterationSerializerTestCase(TestCase):
    def setUp(self):
        self.valid_user_data = {
            "username": "new_user",
            "password": "securepassword123"
        }
        self.invalid_user_data = {
            "username": "new_user",
            "password": "short"  # too short
        }

    def test_valid_registeration_serializer(self):
        serializer = RegisterationSerializer(data=self.valid_user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, self.valid_user_data["username"])
        self.assertTrue(user.check_password(self.valid_user_data["password"]))

    def test_invalid_registeration_serializer(self):
        serializer = RegisterationSerializer(data=self.invalid_user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
