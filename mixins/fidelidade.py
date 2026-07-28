class FidelidadeMixin:

    DESCONTO_FIDELIDADE = 0.10

    def aplicar_desconto_fidelidade(self, valor, quantidade_alugueis):
        if quantidade_alugueis > 3:
            return valor * (1 - self.DESCONTO_FIDELIDADE)

        return valor
