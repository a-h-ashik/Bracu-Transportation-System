from django.urls import path
from .views import homePage
urlpatterns = [
    # Urls added by ashik
    path('home/', homePage, name="homepage"),
    path('home/<id>/<user_type>', homePage, name="homepage"),

    # Urls added by ? 
]
