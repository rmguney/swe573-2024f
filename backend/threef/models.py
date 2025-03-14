from django.db import models
from django.utils import timezone

class Thread(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    tags = models.JSONField()  # IDs like ["Q16338", "Q204370"]
    labels = models.JSONField(blank=True, null=True)  # Labels for corresponding q codes in the tags field
    imageSrc = models.CharField(max_length=500)
    postedBy = models.CharField(max_length=255)
    postedDate = models.DateTimeField(default=timezone.now)
    voteCount = models.IntegerField(default=0)  # Stores total votes for a thread
    material = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    shape = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    texture = models.CharField(max_length=255, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    smell = models.CharField(max_length=255, blank=True, null=True)
    marking = models.CharField(max_length=255, blank=True, null=True)
    functionality = models.CharField(max_length=255, blank=True, null=True)
    period = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    thread = models.ForeignKey(Thread, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies'
    )  # Self-referential field for nested comments
    comment = models.TextField()
    voteCountComment = models.IntegerField(default=0)  # Stores total votes for a comment
    commentator = models.CharField(max_length=255)
    postedDateComment = models.DateTimeField(default=timezone.now)
    selected = models.BooleanField(default=False)

    def __str__(self):
        if self.parent:
            return f'Reply by {self.commentator} to {self.parent.comment}'
        return f'Comment by {self.commentator} on {self.thread.title}'
