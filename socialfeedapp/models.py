from django.db import models
from django.contrib.auth.models import User

class AppGroup(models.Model):
    # Meta
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owners')
    users = models.ManyToManyField(User)
    # Data
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class FeedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    group = models.ForeignKey(AppGroup, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pk}:{self.title}, by {self.user}"