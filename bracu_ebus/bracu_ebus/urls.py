from django.urls import path, include


urlpatterns = [
    path('user/', include('user.urls')),
    path('admin/', include('admin_panel.urls')),
    path('', include('homepage.urls')),
    path('', include('ticket_booking.urls')),
]
