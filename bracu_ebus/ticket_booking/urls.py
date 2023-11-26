from django.urls import path
from .views import interface, seating_cart, booking_form

urlpatterns = [
    # Urls added by ashik
    path('buses/<id>', interface, name="buses"),
    path('seating-cart/<id>/<bus_number>', seating_cart, name="cart"),
    path('booking-form/<id>/<bus_number>/<seat_number>', booking_form, name="booking-form"),

]
