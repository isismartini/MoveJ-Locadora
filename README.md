# Locadora de Veículos MoveJá

## Sobre
A MoveJá é uma locadora de veículos que atua no mercado há anos, oferecendo carros, motos e caminhões para aluguel. Com a expansão do negócio, a empresa contratou a equipe de desenvolvedores para construir um sistema que organize a frota e calcule os valores de aluguel automaticamente, de forma correta para cada tipo de veículo.

## Funcionalidades
- Cálculo automático da diária de aluguel, de acordo com o tipo de veículo (carro, moto ou caminhão)
- Controle da frota de veículos disponíveis
- Registro do histórico de aluguéis de cada cliente
- Aplicação de taxas e descontos conforme as regras de negócio

## Regras de Negócio
1. O cálculo da diária muda conforme o tipo de veículo:
   - Carros têm uma diária fixa
   - Motos têm uma diária mais barata, mas com taxa extra se o cliente não tiver mais de 2 anos de habilitação
   - Caminhões têm diária mais cara e exigem categoria de CNH específica (categoria C ou superior) para serem alugados
2. Existe uma taxa extra de 15% sobre o valor total se o veículo for devolvido com o tanque vazio ou sujo
3. Clientes com mais de 3 aluguéis anteriores na locadora ganham 10% de desconto no valor final do aluguel

## Estrutura do Projeto
- Uma classe abstrata `Veiculo` com métodos abstratos como `calcular_valor_diaria()` e `requisitos_para_dirigir()`
- Classes filhas como `Carro`, `Moto`, `Caminhao`, cada uma com sua própria lógica de cálculo

