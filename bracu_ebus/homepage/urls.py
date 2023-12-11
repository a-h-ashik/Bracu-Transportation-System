from django.urls import path
from .views import homePage, ticketPage, cancelTicket, showpoints,itemshow,complainshow


urlpatterns = [
    # Urls added by ashik
    path('home/', homePage, name="homepage"),
    path('home/<id>', homePage, name="homepage"),
    path('ticket/<id>', ticketPage, name="ticket"),
    path('cancel-ticket/<id>/<ticket_id>', cancelTicket, name="cancel-ticket"),

    path('showpoints/<id>', showpoints, name="showpoints"),
    path('lostitem/<id>', itemshow, name="lostitem"),
    path('complainshow/', complainshow, name="complainshow"),
]
