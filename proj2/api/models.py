from django.db import models

# Create your models here.

class Item(models.Model):
    category = models.CharField(max_length = 225)
    subcategory = models.CharField(max_length = 225)
    name = models.CharField(max_length = 225)
    amount = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.name
