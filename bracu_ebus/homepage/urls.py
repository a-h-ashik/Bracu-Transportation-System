from django.urls import path
from .views import homePage, ticketPage, cancelTicket

urlpatterns = [
    # Urls added by ashik
    path('home/', homePage, name="homepage"),
    path('home/<id>', homePage, name="homepage"),
    path('ticket/<id>', ticketPage, name="ticket"),
    path('cancel-ticket/<id>/<ticket_id>', cancelTicket, name="cancel-ticket"),

]
