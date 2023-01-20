from django.db import models

class Dummydata(models.Model):
    product_id=models.FloatField()
    product_name=models.CharField(max_length=40)
    product_ordered = models.BooleanField(default=False)
    product_quantity = models.IntegerField(default=1)
    





