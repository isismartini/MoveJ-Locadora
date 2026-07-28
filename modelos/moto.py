from .veiculo import Veiculo
from mixins.vistoria import VistoriaMixin


class Moto(Veiculo, VistoriaMixin):

    VALOR_DIARIA = 70.00
    TAXA_NOVO_MOTOCICLISTA = 0.15

    def calcular_valor_diaria(self):
        return self.VALOR_DIARIA

    def requisitos_para_dirigir(self):
        return "CNH categoria A."

    def calcular_valor_com_taxa_habilitacao(self, anos_habilitacao):
        valor = self.calcular_valor_diaria()

        if anos_habilitacao <= 2:
            valor += valor * self.TAXA_NOVO_MOTOCICLISTA

        return valor

    def __str__(self):
        return (
            super().__str__()
            + f" | Diária base: R$ {self.calcular_valor_diaria():.2f}"
        )
