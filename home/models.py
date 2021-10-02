from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=122)
    mobile = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
   

    def __str__(self):
       return self.name
   