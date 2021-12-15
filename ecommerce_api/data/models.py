import uuid
from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    img = models.ImageField(blank=True, null=True)


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField()
    features = models.TextField()
    img = models.ImageField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    weight = models.IntegerField()
    dimentions = models.IntegerField()
    color = models.CharField(max_length=150)
    materials = models.CharField(max_length=150)
    size = models.CharField(max_length=150)
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField()


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    review = models.TextField()
    stars = models.IntegerField()
