from django.db import models
from listings.models import Plans

# Create your models here.
class Booking(models.Model):
    booking_id = models.IntegerField()
    plan_id = models.IntegerField()