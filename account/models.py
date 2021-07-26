from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Product
# Create your models here.
class User(AbstractUser) :
    university = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to="user/", null=True)

class Order(models.Model):
    order_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__ (self):
        return self.order_product.product_name