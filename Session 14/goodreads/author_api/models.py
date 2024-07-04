from django.db import models

class Author(models.Model):
    id = models.UUIDField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    profile_image = models.URLField(null=True, blank=True)
    biography = models.TextField()
    website = models.URLField(null=True, blank=True) 

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
