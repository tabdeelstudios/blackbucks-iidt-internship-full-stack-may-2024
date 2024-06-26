import uuid
from django.db import models

class NoteModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    status = models.BooleanField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notes'
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.title
