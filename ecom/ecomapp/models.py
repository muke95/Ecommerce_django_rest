from django.db import models
from django.utils.timezone import now
# Create your models here.


class User(models.Model):
    # Assuming you already have a User model (or use django.contrib.auth.models.User)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    # etc.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class products(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    discount_percentage = models.FloatField(null=False)
    rating = models.FloatField(null=False)
    stock = models.IntegerField(null=False)
    brand = models.CharField(null=False)
    thumbnail =  models.ImageField(upload_to='product_image/', null=True, blank=True)
    images =   models.ImageField(upload_to='product_image/', null=True, blank=True)
    is_published = models.BooleanField(null=True)
    created_at =models.DateTimeField(default=now, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    def __str__(self):
        return self.title



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(products, on_delete=models.CASCADE, null=True)  # TEMPORARY
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product.title if self.product else 'No Product'}"