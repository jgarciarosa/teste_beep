from django.db import models
from datetime import date
import requests

hoje = date.today()
dia1 = date.fromordinal(hoje.toordinal() - 6)
dias = []

key = '9a4209e2e5de1f04de3b3156ee740e07'


brl_cotacoes = []
ars_cotacoes = []
eur_cotacoes = []

for i in range(0, 7):
    parametros = {'access_key': key, 'date': dia1, 'source': 'USD', 'currencies': 'BRL,ARS,EUR'}
    requisicao = requests.get('http://apilayer.net/api/historical', params=parametros)
    json_data = requisicao.json()
    brl_cotacoes.append(json_data['quotes']['USDBRL'])
    ars_cotacoes.append(json_data['quotes']['USDARS'])
    eur_cotacoes.append(json_data['quotes']['USDEUR'])
    dias.append(str(dia1))
    dia1 = date.fromordinal(dia1.toordinal() + 1)


BRL = {'nome': 'Real(BRL)', 'dado': brl_cotacoes}
ARS = {'nome': 'Peso Argentino(ARS)', 'dado': ars_cotacoes}
EUR = {'nome': 'Euro(EUR)', 'dado': eur_cotacoes}

cotacoes = {'BRL': BRL, 'ARS': ARS, 'EUR': EUR, 'DIAS': dias}
