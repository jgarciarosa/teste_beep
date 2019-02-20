import unittest
from cotacao import models
from cotacao import views

class TesteModels(unittest.TestCase):

    def teste_requisicao_igual_duzentos(self):
        self.assertEqual(200, models.requisicao.status_code)

    def teste_quantidade_dias_igual_sete(self):
        self.assertEqual(7, len(models.dias))

    def teste_quantidade_cotacoes_igual_sete(self):
        self.assertEqual(7, len(models.brl_cotacoes))
        self.assertEqual(7, len(models.ars_cotacoes))
        self.assertEqual(7, len(models.eur_cotacoes))




