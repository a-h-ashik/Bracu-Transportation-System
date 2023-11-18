from django.urls import path
from .views import registration, login, logout, requestAccount

urlpatterns = [
    path('register/', registration, name="register"),
    path('login/', login, name="login"),
    path('login/<msg>', login, name="login"),
    path('logout/<str:id>/', logout, name="logout"),
    path('request-account/', requestAccount, name="requestacc"),
    path('request-account/<msg>', requestAccount, name="requestacc"),
]
