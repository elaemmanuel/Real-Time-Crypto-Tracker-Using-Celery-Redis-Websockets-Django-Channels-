from django.urls import path
from . import views

urlpatterns = [
    path('cryptos/', views.crypto_list, name='crypto_list'),
]