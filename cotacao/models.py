from django.db import models


class Moeda(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nome} - {self.sigla}'


class Cotacao(models.Model):
    moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE)
    data_cotacao = models.CharField(max_length=200)
    valor_cotacao = models.DecimalField(decimal_places=6, max_digits=7, default=0)

    def __str__(self):
        return f'{self.moeda} - {self.data_cotacao} - {self.valor_cotacao}'
















# from datetime import date
# import requests
#
# #seta a data inicial das cotações
# hoje = date.today()
# dia1 = date.fromordinal(hoje.toordinal() - 6)
# dias = []
#
# #chave para requisição do currencylayer
# key = 'a0b70a88d40ae4f5226e23d401b4ab94'
#
#
# brl_cotacoes = []
# ars_cotacoes = []
# eur_cotacoes = []
#
# #itera as listas com os dados retornados da api
# for i in range(0, 7):
#     #requisição a api do currencylayer
#     parametros = {'access_key': key, 'date': dia1, 'source': 'USD', 'currencies': 'BRL,ARS,EUR'}
#     requisicao = requests.get('http://apilayer.net/api/historical', params=parametros)
#     json_data = requisicao.json()
#     brl_cotacoes.append(json_data['quotes']['USDBRL'])
#     ars_cotacoes.append(json_data['quotes']['USDARS'])
#     eur_cotacoes.append(json_data['quotes']['USDEUR'])
#     dias.append(str(dia1))
#     dia1 = date.fromordinal(dia1.toordinal() + 1)
#
#
# BRL = {'nome': 'Real(BRL)', 'dado': brl_cotacoes}
# ARS = {'nome': 'Peso Argentino(ARS)', 'dado': ars_cotacoes}
# EUR = {'nome': 'Euro(EUR)', 'dado': eur_cotacoes}
#
# #dicionário passado como dados json pela view get_dados
# cotacoes = {'BRL': BRL, 'ARS': ARS, 'EUR': EUR, 'DIAS': dias}
