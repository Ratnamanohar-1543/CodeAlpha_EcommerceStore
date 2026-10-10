from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=0)
    old_price = models.DecimalField(max_digits=8, decimal_places=0, null=True, blank=True)
    image_url = models.URLField()
    rating = models.FloatField(default=4.0)
    stock = models.PositiveIntegerField(default=20)
    @property
    def discount(self):
        return int(100 - self.price * 100 / self.old_price) if self.old_price else 0
    def __str__(self): return self.name
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=0)
    address = models.TextField()
    status = models.CharField(max_length=20, default="Placed")
    created = models.DateTimeField(auto_now_add=True)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=0)
