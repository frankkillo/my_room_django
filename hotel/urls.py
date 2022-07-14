from django.urls import path

from .views import search, get_hotel_photos


urlpatterns = [
    path('search/', search, name='search_hotels'),
    path('<int:id>/photos/', get_hotel_photos, name='hotel-photos')
]