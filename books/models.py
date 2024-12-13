import uuid
from accounts.models import User
from django.db import models


class Book(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


