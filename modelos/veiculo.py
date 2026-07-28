from abc import ABC, abstractmethod


class Veiculo(ABC):

    def __init__(self, placa, modelo, ano):
        self.__placa = placa
        self.__modelo = modelo
        self.__ano = ano
        self.__disponivel = True

    @property
    def placa(self):
        return self.__placa

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, valor):
        self.__disponivel = valor

    @abstractmethod
    def calcular_valor_diaria(self):
        pass

    @abstractmethod
    def requisitos_para_dirigir(self):
        pass

    def __str__(self):
        status = "Disponível" if self.disponivel else "Alugado"

        return (
            f"{self.__class__.__name__} | "
            f"Placa: {self.placa} | "
            f"Modelo: {self.modelo} | "
            f"Ano: {self.ano} | "
            f"Status: {status}"
        )
