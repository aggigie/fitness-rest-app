from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}:{self.name}  -  {str(self.calories)} cal/100g"

    class Meta:
        ordering = ['name']

