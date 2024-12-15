import uuid
from accounts.models import User
from bookshelves.models import Bookshelf
from django.db import models


class Book(models.Model):
    READING_STATUS = [
        ('not_started', 'Not Started'),
        ('reading', 'Reading'),
        ('completed', 'Completed')
    ]

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=READING_STATUS, default='not_started')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


