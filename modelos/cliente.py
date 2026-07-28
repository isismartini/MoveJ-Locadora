class Cliente:

    def __init__(self, nome, cpf, categoria_cnh, anos_habilitacao):
        self.__nome = nome
        self.__cpf = cpf
        self.__categoria_cnh = categoria_cnh.upper()
        self.__anos_habilitacao = anos_habilitacao
        self.__historico_alugueis = []

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def categoria_cnh(self):
        return self.__categoria_cnh

    @categoria_cnh.setter
    def categoria_cnh(self, valor):
        self.__categoria_cnh = valor.upper()

    @property
    def anos_habilitacao(self):
        return self.__anos_habilitacao

    @property
    def historico_alugueis(self):
        return self.__historico_alugueis

    def adicionar_aluguel(self, aluguel):
        self.__historico_alugueis.append(aluguel)

    def quantidade_alugueis(self):
        return len(self.__historico_alugueis)

    def possui_desconto_fidelidade(self):
        return self.quantidade_alugueis() > 3

    def __str__(self):
        return (
            f"Cliente: {self.nome} | "
            f"CPF: {self.cpf} | "
            f"CNH: {self.categoria_cnh} | "
            f"Anos de habilitação: {self.anos_habilitacao} | "
            f"Aluguéis anteriores: {self.quantidade_alugueis()}"
        )
