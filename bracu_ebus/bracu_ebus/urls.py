from django.urls import path, include

from stuff_panel import views

urlpatterns = [
    path('user/', include('user.urls')),
    path('admin/', include('admin_panel.urls')),
    path('', include('homepage.urls')),
    path('', include('ticket_booking.urls')),
    path('', include('payment.urls')), #my
    
    

    path('stuff_login/', views.login, name="staff_login"),
    path('stuff_panel/', views.add_show, name="addandshow"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    
    path('shownotificationform/', views.shownotificationform, name="shownotificationform"),
 
    path('givenotification/<id>', views.givenotification, name="givenotification"),
    path('stuffaddpoint/', views.pointadding, name="stuffaddpoint"),
]
