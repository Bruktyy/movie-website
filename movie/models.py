from django.db import models

# Create your models here.


class movies(models.Model):
   product_name = models.CharField(max_length=100)
   product_description = models.TextField()   
   genre = models.CharField(max_length=100)
   image  = models.ImageField(null=True)
   price   = models.FloatField(null=True)
   date   = models.DateTimeField(auto_now_add=True, null=True)
   
   def __str__(self) -> str:
      return self.product_name
   
class about(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()

    def str(self) -> str:
        return self.name