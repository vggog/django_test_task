from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    # In the database the price is stored in cents.
    price = models.IntegerField()
    price_id = models.TextField()
