import datetime
from django.db import models
from django.utils import timezone
from PIL import Image
import os
import tempfile
from django.core.files.base import File
from django.contrib.auth.models import User

class Picture(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def save(self, **kwargs):
        super(Picture, self).save(**kwargs)
        path = self.image.path
        i = Image.open(path)
        i.thumbnail((94 ,94), Image.BILINEAR)
        i.save(path)
    def __unicode__(self):
        return self.name


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
    image_file = models.ForeignKey(Picture)
    price = models.FloatField()
    pub_date = models.DateTimeField('date published')

    
    def __unicode__(self):
        return self.name

class ShoppingCart(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    def __unicode__(self):
        return self.product.name;
