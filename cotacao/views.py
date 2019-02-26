from django.shortcuts import render
from django.http import JsonResponse
from cotacao import services


def index(request):
    return render(request, 'index.html')


def get_dados(request):
    return JsonResponse(services.cotacoes)
