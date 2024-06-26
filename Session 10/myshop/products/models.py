from django.db import models

# Create your models here.
class ProductModel(models.Model):
    productName = models.CharField(max_length=200, unique=True)
    productDescription = models.TextField()
    category = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products'
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.productName