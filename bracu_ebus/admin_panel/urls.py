from django.urls import path
from .views import adminPage, userTable, staffTable, adminLogin
urlpatterns = [
    path('', adminPage, name="admin"),
    path('login/', adminLogin, name="admin_login"),
    path('all-users/', userTable, name="all_users"),
    path('all-staffs/', staffTable, name="all_staffs"),
]
