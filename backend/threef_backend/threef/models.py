from django.db import models
from django.utils import timezone

class Thread(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.JSONField()  # IDs like ["Q16338", "Q204370"]
    imageSrc = models.ImageField(upload_to='images/')
    postedBy = models.CharField(max_length=255)
    postedDate = models.DateTimeField(default=timezone.now)
    voteCount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    thread = models.ForeignKey(Thread, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    voteCountComment = models.IntegerField(default=0)
    commentator = models.CharField(max_length=255)
    postedDateComment = models.DateTimeField(default=timezone.now)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.commentator} on {self.thread.title}'
