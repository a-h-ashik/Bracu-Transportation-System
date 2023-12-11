from django.urls import path
from .views import adminPage, userTable, staffTable, adminLogin, adminLogout, deleteBus, deleteStaff, deleteUser, accountRequestTable, deleteAccountRequest, busTable, admin_add_points
urlpatterns = [
    path('', adminPage, name="admin"),
    path('login/', adminLogin, name="admin_login"),
    path('logout/', adminLogout, name="admin_logout"),
    path('all-users/', userTable, name="all_users"),
    path('delete-user/<id>/', deleteUser, name="delete_user"),
    path('all-staffs/', staffTable, name="all_staffs"),
    #my
    path('delete-staffs/<id>', deleteStaff, name="delete_staff"),

    path('all-account-requests/', accountRequestTable, name="all_account_requests"),
    path('delete-account-requests/<email>', deleteAccountRequest, name="delete_account_request"),

    path('all-routes/', busTable, name="all_routes"),
    path('delete-buses/<id>', deleteBus, name="delete_bus"),
    #my
    path('admin_add_points/<str:user_id>/', admin_add_points, name='admin_add_points'),
]
