from django.db import models

class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    
