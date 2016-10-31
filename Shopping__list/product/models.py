from django.db import models

def product_image_path(instance, filename):
    return 'product-images/{}'.format(filename)

class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    is_complete = models.BooleanField(default=False)
    image = models.ImageField(upload_to=product_image_path, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
