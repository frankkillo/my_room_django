from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Hotel, HotelPhoto


class HotelPhotoSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__300x200")
        ],
        read_only=True
    )

    class Meta:
        model = HotelPhoto
        fields = [
            "id",
            "image"
        ]

    
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = [
            "id",
            "name",
            "location_id",
            "price_from",
            "price_avg",
            "stars",
            "country",
            "place",
            "geo_lond",
            "geo_lat",
        ]