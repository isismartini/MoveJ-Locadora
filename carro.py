from .veiculo import Veiculo
from mixins.vistoria import VistoriaMixin


class Carro(Veiculo, VistoriaMixin):

    VALOR_DIARIA = 100.00

    def calcular_valor_diaria(self):
        return self.VALOR_DIARIA

    def requisitos_para_dirigir(self):
        return "CNH categoria B ou superior."

    def __str__(self):
        return (
            super().__str__()
            + f" | Diária: R$ {self.calcular_valor_diaria():.2f}"
        )
