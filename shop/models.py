from django.db import models

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.title
    title=models.CharField()
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField()
    description=models.TextField()
    image=models.CharField()

class Order(models.Model):
    def __str__(self):
        return self.name
    product_id = models.IntegerField(null=True, blank=True)
    items=models.CharField()
    name=models.CharField()
    email=models.CharField()
    address=models.CharField()
    address2=models.CharField()
    city=models.CharField()
    state=models.CharField()
    zipcode=models.CharField()
    total=models.CharField()