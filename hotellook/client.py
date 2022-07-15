import requests


class HlookHotel:
    def __init__(self, data):
        self.data = data

    @property
    def id(self):
        return self.data["hotelId"]

    @property
    def name(self):
        return self.data["hotelName"]

    @property
    def location_id(self):
        return self.data["locationId"]

    @property
    def price_from(self):
        return self.data["priceFrom"]

    @property
    def price_avg(self):
        return self.data["priceAvg"]

    @property
    def stars(self):
        return self.data["stars"]

    @property
    def country(self):
        return self.data["location"]["country"]

    @property
    def state(self):
        return self.data["location"]["state"]

    @property
    def place(self):
        return self.data["location"]["name"]

    @property
    def geo_long(self):
        return self.data["location"]["geo"]["lon"]

    @property
    def geo_lat(self):
        return self.data["location"]["geo"]["lat"]


def search_hotels(location, check_in, check_out):
    url = 'http://engine.hotellook.com/api/v2/cache.json?currency=rub&limit=10'

    resp = requests.get(url+'&location='+location+'&checkIn='+check_in+'&checkOut='+check_out)
    resp.raise_for_status()
    resp_data = resp.json()

    for hotel in resp_data:
        yield HlookHotel(hotel)

def get_hotels_photos(hotel_id):
    resp = requests.get(f'https://yasen.hotellook.com/photos/hotel_photos?id={hotel_id}')
    resp.raise_for_status()
    resp_data = resp.json()
    
    return resp_data[str(hotel_id)]

def get_photo(photo_id):
    resp = requests.get(f'https://photo.hotellook.com/image_v2/limit/{photo_id}/800/520.auto')
    resp.raise_for_status()
    
    return resp.content
