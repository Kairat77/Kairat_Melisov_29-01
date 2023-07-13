
from django.db import models


class Icon(models.Model):
    icon = models.ImageField(upload_to="photos", verbose_name="Фото")

class Product(models.Model):
    image = models.ImageField(upload_to="photos",verbose_name="Фото")
    title = models.CharField(max_length=256)
    description = models.TextField()
    

    @property
    def icons_list(self) ->list:
        return self.icons.all()


    
