from modelos import (
    Carro,
    Moto,
    Caminhao,
    Cliente,
    Aluguel
)


def mostrar_titulo():
    print("\n" + "=" * 50)
    print("        MOVEJÁ LOCADORA DE VEÍCULOS")
    print("=" * 50)


def mostrar_veiculos(frota):
    print("\n--- FROTA ---")

    for indice, veiculo in enumerate(frota, start=1):
        print(f"{indice}. {veiculo}")


def cadastrar_veiculo(frota):
    print("\n--- CADASTRAR VEÍCULO ---")

    print("1 - Carro")
    print("2 - Moto")
    print("3 - Caminhão")

    tipo = input("Escolha o tipo: ")
    placa = input("Digite a placa: ")
    modelo = input("Digite o modelo: ")

    try:
        ano = int(input("Digite o ano: "))
    except ValueError:
        print("Ano inválido.")
        return

    if tipo == "1":
        veiculo = Carro(placa, modelo, ano)

    elif tipo == "2":
        veiculo = Moto(placa, modelo, ano)

    elif tipo == "3":
        veiculo = Caminhao(placa, modelo, ano)

    else:
        print("Tipo inválido.")
        return

    frota.append(veiculo)

    print("\nVeículo cadastrado com sucesso!")


def cadastrar_cliente(clientes):
    print("\n--- CADASTRAR CLIENTE ---")

    nome = input("Nome: ")
    cpf = input("CPF: ")
    categoria = input("Categoria da CNH: ").upper()

    try:
        anos = int(input("Anos de habilitação: "))
    except ValueError:
        print("Valor inválido.")
        return

    cliente = Cliente(
        nome,
        cpf,
        categoria,
        anos
    )

    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!")


def realizar_aluguel(frota, clientes, alugueis):
    print("\n--- NOVO ALUGUEL ---")

    if not frota:
        print("Não existem veículos cadastrados.")
        return

    if not clientes:
        print("Não existem clientes cadastrados.")
        return

    print("\nClientes:")

    for indice, cliente in enumerate(clientes, start=1):
        print(f"{indice}. {cliente}")

    try:
        cliente_indice = int(input("Escolha o cliente: ")) - 1
        cliente = clientes[cliente_indice]
    except (ValueError, IndexError):
        print("Cliente inválido.")
        return

    veiculos_disponiveis = [
        veiculo
        for veiculo in frota
        if veiculo.disponivel
    ]

    if not veiculos_disponiveis:
        print("Não existem veículos disponíveis.")
        return

    print("\nVeículos disponíveis:")

    for indice, veiculo in enumerate(
        veiculos_disponiveis,
        start=1
    ):
        print(f"{indice}. {veiculo}")

    try:
        veiculo_indice = int(
            input("Escolha o veículo: ")
        ) - 1

        veiculo = veiculos_disponiveis[veiculo_indice]

    except (ValueError, IndexError):
        print("Veículo inválido.")
        return

    try:
        dias = int(input("Quantidade de dias: "))

        if dias <= 0:
            print("A quantidade de dias deve ser maior que zero.")
            return

    except ValueError:
        print("Quantidade de dias inválida.")
        return

    aluguel = Aluguel(
        cliente,
        veiculo,
        dias
    )

    try:
        valor = aluguel.calcular_valor()

        veiculo.disponivel = False

        alugueis.append(aluguel)

        print("\nALUGUEL REALIZADO!")
        print(f"Cliente: {cliente.nome}")
        print(f"Veículo: {veiculo.modelo}")
        print(f"Dias: {dias}")
        print(f"Valor total: R$ {valor:.2f}")

        if cliente.possui_desconto_fidelidade():
            print("Desconto de fidelidade aplicado!")

    except ValueError as erro:
        print(f"\nErro: {erro}")


def finalizar_aluguel(alugueis):
    print("\n--- FINALIZAR ALUGUEL ---")

    alugueis_ativos = [
        aluguel
        for aluguel in alugueis
        if not aluguel.finalizado
    ]

    if not alugueis_ativos:
        print("Não existem aluguéis ativos.")
        return

    for indice, aluguel in enumerate(
        alugueis_ativos,
        start=1
    ):
        print(
            f"{indice}. "
            f"{aluguel.cliente.nome} - "
            f"{aluguel.veiculo.modelo} - "
            f"R$ {aluguel.valor_total:.2f}"
        )

    try:
        escolha = int(
            input("Escolha o aluguel: ")
        ) - 1

        aluguel = alugueis_ativos[escolha]

    except (ValueError, IndexError):
        print("Aluguel inválido.")
        return

    tanque = input(
        "O veículo foi devolvido com o tanque vazio? (s/n): "
    ).lower()

    sujo = input(
        "O veículo foi devolvido sujo? (s/n): "
    ).lower()

    tanque_vazio = tanque == "s"
    veiculo_sujo = sujo == "s"

    aluguel.finalizar_aluguel(
        tanque_vazio,
        veiculo_sujo
    )

    print("\nAluguel finalizado!")

    print(
        f"Valor final: "
        f"R$ {aluguel.valor_total:.2f}"
    )

    print(
        f"Vistoria: "
        f"{aluguel.veiculo.descricao_vistoria()}"
    )


def mostrar_clientes(clientes):
    print("\n--- CLIENTES ---")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(cliente)


def mostrar_alugueis(alugueis):
    print("\n--- HISTÓRICO DE ALUGUÉIS ---")

    if not alugueis:
        print("Nenhum aluguel registrado.")
        return

    for aluguel in alugueis:
        status = (
            "Finalizado"
            if aluguel.finalizado
            else "Ativo"
        )

        print(
            f"Cliente: {aluguel.cliente.nome} | "
            f"Veículo: {aluguel.veiculo.modelo} | "
            f"Dias: {aluguel.dias} | "
            f"Valor: R$ {aluguel.valor_total:.2f} | "
            f"Status: {status}"
        )


def menu():
    frota = []
    clientes = []
    alugueis = []

    frota.append(
        Carro(
            "ABC-1234",
            "Volkswagen Gol",
            2022
        )
    )

    frota.append(
        Moto(
            "XYZ-5678",
            "Honda CG 160",
            2023
        )
    )

    frota.append(
        Caminhao(
            "CAM-9999",
            "Volkswagen Delivery",
            2021
        )
    )

    while True:

        mostrar_titulo()

        print("\n1 - Mostrar frota")
        print("2 - Cadastrar veículo")
        print("3 - Cadastrar cliente")
        print("4 - Realizar aluguel")
        print("5 - Finalizar aluguel")
        print("6 - Mostrar clientes")
        print("7 - Mostrar histórico de aluguéis")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            mostrar_veiculos(frota)

        elif opcao == "2":
            cadastrar_veiculo(frota)

        elif opcao == "3":
            cadastrar_cliente(clientes)

        elif opcao == "4":
            realizar_aluguel(
                frota,
                clientes,
                alugueis
            )

        elif opcao == "5":
            finalizar_aluguel(alugueis)

        elif opcao == "6":
            mostrar_clientes(clientes)

        elif opcao == "7":
            mostrar_alugueis(alugueis)

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    menu()
