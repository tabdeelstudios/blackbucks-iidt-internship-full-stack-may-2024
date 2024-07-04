from django.db import models

class Book(models.Model):
    id = models.UUIDField(unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    publication_date = models.DateField(null=True, blank=True)
    cover_image = models.URLField()
    genre = models.CharField(max_length=50)
    summary = models.TextField()

    def __str__(self) -> str:
        return self.title