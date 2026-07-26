class VistoriaMixin:

    def registrar_vistoria_devolucao(self, tanque_vazio=False, veiculo_sujo=False):
        self.__tanque_vazio = tanque_vazio
        self.__veiculo_sujo = veiculo_sujo

    def devolucao_com_problema(self):
        return self.__tanque_vazio or self.__veiculo_sujo

    def calcular_taxa_devolucao(self, valor):
        if self.devolucao_com_problema():
            return valor * 0.15

        return 0.0

    def descricao_vistoria(self):
        tanque = getattr(self, "_VistoriaMixin__tanque_vazio", False)
        sujo = getattr(self, "_VistoriaMixin__veiculo_sujo", False)

        if tanque and sujo:
            return "Tanque vazio e veículo sujo."

        if tanque:
            return "Tanque vazio."

        if sujo:
            return "Veículo sujo."

        return "Veículo devolvido em boas condições."
