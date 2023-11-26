from django.urls import path
from .views import adminPage, userTable, staffTable, adminLogin, adminLogout, deleteUser, accountRequestTable, deleteAccountRequest, busTable
urlpatterns = [
    path('', adminPage, name="admin"),
    path('login/', adminLogin, name="admin_login"),
    path('logout/', adminLogout, name="admin_logout"),
    path('all-users/', userTable, name="all_users"),
    path('delete-user/<id>/', deleteUser, name="delete_user"),
    path('all-staffs/', staffTable, name="all_staffs"),
    path('all-account-requests/', accountRequestTable, name="all_account_requests"),
    path('delete-account-requests/<email>', deleteAccountRequest, name="delete_account_request"),

    path('all-routess/', busTable, name="all_routes"),
]
