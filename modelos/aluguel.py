from mixins.fidelidade import FidelidadeMixin


class Aluguel(FidelidadeMixin):

    def __init__(self, cliente, veiculo, dias):
        self.__cliente = cliente
        self.__veiculo = veiculo
        self.__dias = dias
        self.__valor_total = 0.0
        self.__finalizado = False

    @property
    def cliente(self):
        return self.__cliente

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def dias(self):
        return self.__dias

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def finalizado(self):
        return self.__finalizado

    def verificar_requisitos(self):
        if isinstance(self.veiculo, __import__(
            "modelos.caminhao",
            fromlist=["Caminhao"]
        ).Caminhao):

            return self.veiculo.possui_categoria_permitida(
                self.cliente.categoria_cnh
            )

        if self.veiculo.__class__.__name__ == "Moto":
            return self.cliente.categoria_cnh == "A"

        if self.veiculo.__class__.__name__ == "Carro":
            return self.cliente.categoria_cnh in ("B", "C", "D", "E")

        return False

    def calcular_valor(self):
        if not self.verificar_requisitos():
            raise ValueError(
                "O cliente não possui a categoria de CNH necessária "
                "para este veículo."
            )

        valor_diarias = self.veiculo.calcular_valor_diaria() * self.dias

        if self.veiculo.__class__.__name__ == "Moto":
            if self.cliente.anos_habilitacao <= 2:
                valor_diarias *= 1.15

        valor_com_desconto = self.aplicar_desconto_fidelidade(
            valor_diarias,
            self.cliente.quantidade_alugueis()
        )

        self.__valor_total = valor_com_desconto

        return self.__valor_total

    def finalizar_aluguel(self, tanque_vazio=False, veiculo_sujo=False):
        if self.__finalizado:
            raise ValueError("Este aluguel já foi finalizado.")

        self.veiculo.registrar_vistoria_devolucao(
            tanque_vazio,
            veiculo_sujo
        )

        taxa_devolucao = self.veiculo.calcular_taxa_devolucao(
            self.__valor_total
        )

        self.__valor_total += taxa_devolucao

        self.veiculo.disponivel = True
        self.__finalizado = True

        self.cliente.adicionar_aluguel(self)

    def resumo(self):
        return {
            "cliente": self.cliente.nome,
            "veiculo": self.veiculo.modelo,
            "dias": self.dias,
            "valor_total": self.valor_total,
            "finalizado": self.finalizado
        }
