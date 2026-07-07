# 1. Escreva um programa em Python que calcule o desconto/acréscimo para a compra de um determinado produto. Solicite a quantidade de itens, o preço unitário e a forma de pagamento. Informe qual desconto/acréscimo foi aplicado e o valor total da compra, seguindo as regras:

# Pagamento à vista:
# Até 5 itens: 5% de desconto;
# Entre 5 e 10 itens: 8% de desconto;
# Acima de 10 itens: 15% de desconto.

# Pagamento à prazo:
# Até 5 itens: 5% de acréscimo;
# Entre 5 e 10 itens: sem desconto ou acréscimo;
# Acima de 10 itens: 5% de desconto.

# Escreva uma função para calcular o desconto/acréscimo.

produto = input("Qual o nome do produto que você quer comprar?")
qtdade = int(input("Qual a quantidade?"))
precoUni = float(input("Qual o preço unitário dele?"))
pgto = input("Qual a forma de pagamento? Escolha entre à [V]ista ou a [P]razo.").upper()

def calcular_total(qtdade, preco_unitario, forma_pgto):
    total_bruto = qtdade * preco_unitario

    if forma_pgto == 'V':
        # Pagamento à vista
        if qtdade <= 5:
            desconto = 0.05
            tipo = "desconto"
        elif 5 < qtdade <= 10:
            desconto = 0.08
            tipo = "desconto"
        else:  # acima de 10
            desconto = 0.15
            tipo = "desconto"
    elif forma_pgto == 'P':
        # Pagamento a prazo
        if qtdade <= 5:
            desconto = -0.05
            tipo = "acréscimo"
        elif 5 < qtdade <= 10:
            desconto = 0.0
            tipo = "nenhum"
        else:  # acima de 10
            desconto = 0.05
            tipo = "desconto"
    else:
        return None, None, None

    valor_total = total_bruto * (1 - desconto)
    return valor_total, desconto, tipo

# Cálculo
total, desconto, tipo = calcular_total(qtdade, precoUni, pgto)

if total is None:
    print("Opção de pagamento inválida.")
else:
    print(f"\nProduto: {produto}")
    print(f"Quantidade: {qtdade}")
    print(f"Preço unitário: R$ {precoUni:.2f}")
    print(f"Forma de pagamento: {'À vista' if pgto == 'V' else 'À prazo'}")

    if tipo == "nenhum":
        print("Nenhum desconto ou acréscimo foi aplicado.")
    else:
        porcentagem = abs(desconto * 100)
        print(f"{tipo.capitalize()} aplicado: {porcentagem:.0f}%")

    print(f"Valor total da compra: R$ {total:.2f}")


# 2. Escreva um programa em Python que solicite o salário de 5 pessoas da mesma família e, com base nestas informações:

# retorne a média desses salários;
# informe qual salário é o mais alto;
# indique se a média dos salários é superior, igual ou inferior ao salário mínimo (R$ 1518,00).
# Armazene os "salários" em uma lista.

salario_minimo = 1518.00
salarios = []

for i in range(1, 6):
    salario = float(input(f"Digite o salário da {i}ª pessoa: R$ "))
    salarios.append(salario)

media = sum(salarios) / len(salarios)
salario_mais_alto = max(salarios)

if media > salario_minimo:
    comparacao = "superior"
elif media < salario_minimo:
    comparacao = "inferior"
else:
    comparacao = "igual"

print(f"Média dos salários: R$ {media:.2f}")
print(f"Salário mais alto: R$ {salario_mais_alto:.2f}")
print(f"A média dos salários é {comparacao} ao salário mínimo (R$ {salario_minimo:.2f}).")