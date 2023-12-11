from django.urls import path
from .views import payment, charge, generate_pdf

urlpatterns = [
    path('payment/', payment, name='payment'),
    path('charge/', charge, name='charge'),
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
]