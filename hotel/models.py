from django.db import models
from versatileimagefield.fields import VersatileImageField

class Hotel(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    location_id = models.PositiveBigIntegerField()
    price_from = models.DecimalField(max_digits=10, decimal_places=2)
    price_avg = models.DecimalField(max_digits=10, decimal_places=2)
    stars = models.IntegerField()
    country = models.CharField(max_length=150)
    state = models.CharField(max_length=150, blank=True, null=True)
    place = models.CharField(max_length=150)
    geo_lond = models.DecimalField(max_digits=9, decimal_places=6)
    geo_lat = models.DecimalField(max_digits=9, decimal_places=6)



class HotelPhoto(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    hotel = models.ForeignKey(Hotel, related_name='photos', on_delete=models.CASCADE)
    image = VersatileImageField(upload_to="hotel-photos", blank=True, null=True)