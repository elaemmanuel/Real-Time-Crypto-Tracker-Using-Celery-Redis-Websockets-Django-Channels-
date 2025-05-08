from django.shortcuts import render
from .models import Coin

def crypto_list(request):
    coins = Coin.objects.all()
    return render(request, 'crypto_list.html', {'coins': coins})