from django.db import models

# Create your models here.

class Listing(models.Model):
    list_image = models.ImageField(null=True,blank=True)
    address = models.CharField(max_length=255, null=True)


