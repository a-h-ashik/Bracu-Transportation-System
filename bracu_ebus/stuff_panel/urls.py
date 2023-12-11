from django.urls import path
from stuff_panel.views import shownotificationform, givenotification,pointadding


urlpatterns = [
    
    # Urls added by ? 
    
    path('getnotification/', givenotification, name="givenotification"),
    path('shownotificationform/', shownotificationform, name="shownotificationform"),
    path('stuffaddpoint/', pointadding, name="stuffaddpoint"),
    

    
]