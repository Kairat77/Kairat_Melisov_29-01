from django.db import models

class Icon(models.Model):
    icon = models.ImageField()

class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256)
    description = models.TextField()
    icons = models.ManyToManyField(Icon)

    @property
    def icons_list(self) ->list:
        return self.icons.all()
    
