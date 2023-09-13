from django.db import models
class Book(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    price = models.IntegerField()



# Create your models here.
