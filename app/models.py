from django.db import models

class SumResult(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.IntegerField()

