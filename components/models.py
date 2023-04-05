from django.db import models
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/category/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    

class Brand(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/brand/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/category/', blank=True, null=True)
    highlight = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    specification = models.TextField(blank=True, null=True)
    quantity = models.BigIntegerField(blank=True, null=True)
    is_sell = models.BooleanField(default=False)
    discount = models.FloatField(blank=True, null=True)
    is_featured = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    def resize_image(self):
        with Image.open(self.image.path) as img:
            img.thumbnail((275, 210))
            img.save(self.image.path)