from .veiculo import Veiculo
from mixins.vistoria import VistoriaMixin


class Caminhao(Veiculo, VistoriaMixin):

    VALOR_DIARIA = 250.00

    def calcular_valor_diaria(self):
        return self.VALOR_DIARIA

    def requisitos_para_dirigir(self):
        return "CNH categoria C, D ou E."

    def possui_categoria_permitida(self, categoria_cnh):
        categorias_permitidas = ("C", "D", "E")

        return categoria_cnh.upper() in categorias_permitidas

    def __str__(self):
        return (
            super().__str__()
            + f" | Diária: R$ {self.calcular_valor_diaria():.2f}"
        )
