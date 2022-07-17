from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Hotel
from .serializers import HotelSerializer, HotelPhotoSerializer
from .hotellook_integration import search_and_save, hotel_photos


@api_view(['POST'])
def search(request):
    location = request.data.get('location')
    check_in = request.data.get('checkIn')
    check_out = request.data.get('checkOut')

    hotels_ids = search_and_save(location, check_in, check_out)

    hotels = Hotel.objects.filter(id__in=hotels_ids)
    serializer = HotelSerializer(hotels, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_hotel_photos(request, id):
    if hotel_photos(id):
        hotel = Hotel.objects.get(id=id)
        serializer = HotelPhotoSerializer(hotel.photos, many=True)

        return Response(serializer.data)
    
    return Response("Hotel not found", status=status.HTTP_404_NOT_FOUND)