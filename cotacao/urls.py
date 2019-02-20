from django.urls import path
from cotacao import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/data/', views.get_dados, name='api/data')
]