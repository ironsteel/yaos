import datetime
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    description = models.TextField()
    availability = models.IntegerField()
    image_file = models.ImageField(upload_to="images")
    
    def __unicode__(self):
        return self.name



