from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, blank=True)
    province = models.CharField(max_length=100, blank=True)
    post_code = models.CharField(max_length=5, blank=True)
    tel = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

class Product(models.Model):
    name = models.CharField(max_length=20, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.CharField(max_length=255, blank=True)


class Shipping(models.Model):
    method = models.CharField(max_length=255, blank=True)
    fee = models.FloatField()

class Payment(models.Model):
    payment_owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    method = models.CharField(max_length=255, blank=True)
    card_no = models.CharField(max_length=255, blank=True)
    expired = models.CharField(max_length=5, blank=True)
    holder_name = models.CharField(max_length=500, blank=True)

class Order(models.Model):
    total_price = models.FloatField()
    status = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping = models.ForeignKey(Shipping, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_price = models.FloatField()
    quantity = models.IntegerField()



