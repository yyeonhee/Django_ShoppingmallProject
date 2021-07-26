from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_info = models.TextField()
    product_img = models.ImageField(upload_to = "product/", blank=True, null=True )

    def __str__ (self):
        return self.product_name