from django.db import models

class Book(models.Model):

    STATUS_CHOICES = [
        (1, "Active"),
        (0, "Inactive"),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
