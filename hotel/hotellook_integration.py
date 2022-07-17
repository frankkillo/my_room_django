
import tempfile
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from hotellook.client import search_hotels, get_hotels_photos, get_photo
from .models import Hotel, HotelPhoto


def search_and_save(location, check_in, check_out):

    hotels_ids = []
    
    for hotel in search_hotels(location, check_in, check_out):
        obj, created = Hotel.objects.get_or_create(id=hotel.id, 
            defaults={
                "name": hotel.name,
                "location_id": hotel.location_id,
                "price_from": hotel.price_from,
                "price_avg": hotel.price_avg,
                "stars": hotel.stars,
                "country": hotel.country,
                "state": hotel.state,
                "place": hotel.place,
                "geo_lond": hotel.geo_long,
                "geo_lat": hotel.geo_lat
            }
        )

        hotels_ids.append(obj.id)
      
    return hotels_ids


def hotel_photos(hotel_id):
    try:
        hotel = Hotel.objects.get(id=hotel_id)
    except ObjectDoesNotExist:
        return False

    photos_ids = get_hotels_photos(hotel_id)

    for photo_id in photos_ids:
        hotel_photo, created = HotelPhoto.objects.get_or_create(id=photo_id, hotel=hotel)
        if created: 
            bytearray = get_photo(photo_id)
            lf = tempfile.NamedTemporaryFile()
            lf.write(bytearray)
            lf.flush()

            hotel_photo.image.save(
                f'{photo_id}.jpg',
                File(lf, 'rb')
            )
            hotel_photo.save()
    
    return True