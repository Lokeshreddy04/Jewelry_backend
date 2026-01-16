from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    base_metal = models.CharField(max_length=100)
    polish = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    image_url = models.URLField()

    def __str__(self):
        return self.name
