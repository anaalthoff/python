# Funções
# A definição da função deve vir antes de sua chamada

# Exemplo de função
def fatorial(num):
    if num < 0:
        return 0
    if num <= 1:
        return 1
    fat = 1
    for i in range(1, num+1):
        fat *= i
    return fat

# Outro exemplo:
def soma(a, b):
    s = a+b
    return s
# OU

def soma(a, b):
    return (a+b)

x = int(input())
y = int(input())
s = soma(x, y)
print(s)

# Calcular as seguintes áreas: círculo, retângulo, quadradoe  trapézio. Fazer um menu que pergunta ao usuário qual figura ele deseja calcular.
opcao = ''
while opcao != 'S':
    print('\nCalcule a área de:')
    print('[C]írculo')
    print('[R]etângulo')
    print('[Q]uadrado')
    print('[T]rapézio')
    print('[S]air')
    opcao = input('Opção: ').upper()

    if opcao == 'C':
        raio = float(input('Raio do círculo: '))
        area = 3.14 * raio ** 2
        print('A área do círculo é', area)
    elif opcao == 'R':
        base = float(input('Base do retângulo: '))
        altura = float(input('Altura do retângulo: '))
        area = base * altura
        print('A área do retângulo é', area)
    elif opcao == 'Q':
        lado = float(input('Lado do quadrado: '))
        area = lado**2
        print('A área do quadrado é', area)
    elif opcao == 'T':
        baseG = float(input('Base maior do trapézio: '))
        baseP = float(input('Base menor do trapézio: '))
        altura = float(input('Altura do trapézio: '))
        area = (baseG+baseP)/2 * altura
        print('A área do trapézio é', area)
    elif opcao != 'S':
        print('Opção inválida')


# Alterar o programa anterior separando cada um dos cálculos de área em diferentes funções. Essas funções não recebem nenhum valor como parâmetro e também não retornam valores.
def areaCirculo():
    raio = float(input('Raio do círculo: '))
    area = 3.14 * raio ** 2
    print('A área do círculo é', area)

def areaRetangulo():
    base = float(input('Base do retângulo: '))
    altura = float(input('Altura do retângulo: '))
    area = base * altura
    print('A área do retângulo é', area)

def areaQuadrado():
    lado = float(input('Lado do quadrado: '))
    area = lado**2
    print('A área do quadrado é', area)

def areaTrapezio():
    baseG = float(input('Base maior do trapézio: '))
    baseP = float(input('Base menor do trapézio: '))
    altura = float(input('Altura do trapézio: '))
    area = (baseG+baseP)/2 * altura
    print('A área do trapézio é', area)

opcao = ''
while opcao != 'S':
    print('\nCalcule a área de:')
    print('[C]írculo')
    print('[R]etângulo')
    print('[Q]uadrado')
    print('[T]rapézio')
    print('[S]air')
    opcao = input('Opção: ').upper()

    if opcao == 'C':
        areaCirculo()
    elif opcao == 'R':
        areaRetangulo()
    elif opcao == 'Q':
        areaQuadrado()
    elif opcao == 'T':
        areaTrapezio()
    elif opcao != 'S':
        print('Opção inválida')

# Alterar o programa anterior fazendo com que as funções recebam valores como parâmetros e retornem valores.
def areaCirculo(raio):
    area = 3.14 * raio ** 2
    return area

def areaRetangulo(base, altura):
    return base * altura

def areaQuadrado(lado):
    return lado**2

def areaTrapezio(baseG, baseP, altura):
    return (baseG+baseP)/2 * altura

opcao = ''
while opcao != 'S':
    print('\nCalcule a área de:')
    print('[C]írculo')
    print('[R]etângulo')
    print('[Q]uadrado')
    print('[T]rapézio')
    print('[S]air')
    opcao = input('Opção: ').upper()

    if opcao == 'C':
        raio = float(input('Raio do círculo: '))
        area = areaCirculo(raio)
        print('A área do círculo é', area)
    elif opcao == 'R':
        base = float(input('Base do retângulo: '))
        altura = float(input('Altura do retângulo: '))
        area = areaRetangulo(base, altura)
        print('A área do retângulo é', area)
    elif opcao == 'Q':
        lado = float(input('Lado do quadrado: '))
        area = areaQuadrado(lado)
        print('A área do quadrado é', area)
    elif opcao == 'T':
        baseG = float(input('Base maior do trapézio: '))
        baseP = float(input('Base menor do trapézio: '))
        altura = float(input('Altura do trapézio: '))
        area = areaTrapezio(baseG, baseP, altura)
        print('A área do trapézio é', area)
    elif opcao != 'S':
        print('Opção inválida')

# Ler data de nascimento de uma pessoa e exibir quantos dias ela já viveu.
dia = int(input('Que dia você nasceu? '))
mes = int(input('Que mês você nasceu? '))
ano = int(input('Que ano você nasceu? '))

dia_atual = int(input('Dia atual: '))
mes_atual = int(input('Mês atual: '))
ano_atual = int(input('Ano atual: '))

def diasCorridos(dia, mes, ano):
    # mês:         1,  2,  3,  4,  5,   6,   7,   8,   9,  10,  11,  12
    tabelaMeses = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    # Multiplicar por 365.25 leva em conta o ano bissexto, adicionando um quarto de dia extra para cada ano.
    dias = int(ano*365.25)
    dias += tabelaMeses[mes-1]
    if mes > 2 and ano % 4 == 0:
        dias += 1
    # adicionamos os dias do mês corrente
    dias += dia
    return dias

dias = diasCorridos(dia_atual, mes_atual, ano_atual) - \
    diasCorridos(dia, mes, ano)

print(f'Você tem {dias} de vida.')

# Outra forma:
def bissexto(ano):
    # Função para verificar se um ano é bissexto
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def dias_do_mes(mes, ano):
    # Função para obter o número de dias em um mês
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if bissexto(ano) else 28

def dias_corridos(dia, mes, ano):
    # Função para calcular o total de dias decorridos
    total_dias = 0

    # Adicionar dias completos de anos inteiros
    for i in range(ano):
        total_dias += 366 if bissexto(i) else 365

    # Adicionar dias completos de meses inteiros
    for i in range(1, mes):
        total_dias += dias_do_mes(i, ano)

    # Adicionar dias do mês atual
    total_dias += dia

    return total_dias

# Obter a data de nascimento do usuário
dia_nascimento = int(input('Que dia você nasceu? '))
mes_nascimento = int(input('Que mês você nasceu? '))
ano_nascimento = int(input('Que ano você nasceu? '))

# Obter a data atual do usuário
dia_atual = int(input('Dia atual: '))
mes_atual = int(input('Mês atual: '))
ano_atual = int(input('Ano atual: '))

# Calcular dias corridos
dias = dias_corridos(dia_atual, mes_atual, ano_atual) - \
    dias_corridos(dia_nascimento, mes_nascimento, ano_nascimento)

print(f'Você tem {dias} dias de vida.')

# Desenvolva uma função somatorio(n) para calcular a soma de todos os valores ímpares de 1 até o número indicado.
n = int(input('Insira um número: '))

def somatorio(n):
    soma = 0
    for i in range(1, n+1, 2):
        soma += i
    return soma

print(somatorio(n))

# Desenvolva uma função sequencia(n) para calcular a sequência da potência de 2 até o valor informado.
n = int(input('Insira um número: '))
def sequencia(n):
    i = 1
    while 2 ** i <= n:
        print(2 ** i)
        i += 1

sequencia(n)

# Faça uma função chamada multiplos7(inicio,fim) que retorna a SOMA dos múltiplos de 7 entre um valor inicial e um valor final (inclusive).
def multiplos7(inicio, fim):
    soma = 0
    for numero in range(inicio, fim + 1):
        if numero % 7 == 0:
            soma += numero
    return soma

# Exemplo de uso:
inicio = int(input("Informe o valor inicial: "))
fim = int(input("Informe o valor final: "))

resultado = multiplos7(inicio, fim)
print(f"A soma dos múltiplos de 7 entre {inicio} e {fim} é {resultado}.")

# Somar os valores da diagonal principal de uma matriz quadrada.
import random
def criar_matriz (dim):
    matriz = [[random.randint(1,9) for j in range(dim)] for i in range(dim)]
    return matriz

def soma(matriz, dim):
    soma = 0
    for i in range(dim):
        soma += matriz[i][i]
    return soma

dim = int(input('Insira a dimensão da matriz: '))
matriz = criar_matriz(dim)
print(matriz)
print(soma(matriz, dim))

# # Outra forma
# matriz = [[1,2,3],[4,5,6],[7,8,9]]
# soma = 0
# for i in range(3):
#     soma = soma + matriz[i][i]
# print(soma)

# Substituir todos os números negativos de uma matriz por seu módulo
import random
def criar_matriz (dim):
    matriz = [[random.randint(-9,9) for j in range(dim)] for i in range(dim)]
    return matriz

def soma(matriz, dim):
    soma = 0
    for i in range(dim):
        soma += matriz[i][i]
    return soma

def modulo(matriz, dim):
    for i in range(dim):
        for j in range(dim):
            matriz[i][j] = abs(matriz[i][j])

dim = int(input('Insira a dimensão da matriz: '))
matriz = criar_matriz(dim)

print("Matriz original:")
print(matriz)

modulo(matriz, dim)
print("Matriz após aplicar o módulo:")
print(matriz)

print("Soma da diagonal principal após a modificação:")
print(soma(matriz, dim))

# Crie uma função que receba dois números e calcule a exponenciação (potência) do primeiro pelo segundo, ou seja, o primeiro número é a base e o segundo é o expoente. Nome da função: potencia().
def potencia(base, expoente):
    return base ** expoente

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = potencia(base, expoente)
print(f"{base} elevado a {expoente} é igual a {resultado}")

def potencia(base, expoente):
    resultado = base ** expoente
    return resultado

print(potencia(0, 1))

# Faça uma função troca() que recebe uma lista com dois valores e troca o conteúdo dos dois. Ou seja, o primeiro elemento da lista se transforma no segundo e o segundo se transforma no primeiro.
def troca(V):
    aux = V[0]
    V[0] = V[1]
    V[1] = aux

def troca(lista):
    if len(lista) == 2:
        temp = lista[0]
        lista[0] = lista[1]
        lista[1] = temp
    else:
        print("A lista deve conter exatamente dois elementos.")

# Exemplo de uso
minha_lista = random.sample(range(1, 100), 2)
print("Antes da troca:", minha_lista)

troca(minha_lista)
print("Depois da troca:", minha_lista)

# Faça uma função para calcular o fatorial de um número. Receba como parâmetro um número n e retorne como resposta n! Obs.: nome da função deve ser fatorial()
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def fatorial(n):
    resultado=1
    for num in range(1,n+1):
        resultado *= num
    return resultado

def fatorial(n):
    resultado=1
    num=1
    while num <= n:
        resultado *= num
        num += 1
    return resultado

numero = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")

# Crie uma função maior() que recebe três valores e retorna o maior dos três.
def maior(a, b, c):
    return max(a, b, c)

def maior(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c:
        return b
    return c

# Exemplo de uso
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

resultado = maior(num1, num2, num3)
print(f"O maior número é: {resultado}")# Funções
# A definição da função deve vir antes de sua chamada

# Exemplo de função
def fatorial(num):
    if num < 0:
        return 0
    if num <= 1:
        return 1
    fat = 1
    for i in range(1, num+1):
        fat *= i
    return fat

# Outro exemplo:
def soma(a, b):
    s = a+b
    return s
# OU

def soma(a, b):
    return (a+b)

x = int(input())
y = int(input())
s = soma(x, y)
print(s)

# Calcular as seguintes áreas: círculo, retângulo, quadradoe  trapézio. Fazer um menu que pergunta ao usuário qual figura ele deseja calcular.
opcao = ''
while opcao != 'S':
    print('\nCalcule a área de:')
    print('[C]írculo')
    print('[R]etângulo')
    print('[Q]uadrado')
    print('[T]rapézio')
    print('[S]air')
    opcao = input('Opção: ').upper()

    if opcao == 'C':
        raio = float(input('Raio do círculo: '))
        area = 3.14 * raio ** 2
        print('A área do círculo é', area)
    elif opcao == 'R':
        base = float(input('Base do retângulo: '))
        altura = float(input('Altura do retângulo: '))
        area = base * altura
        print('A área do retângulo é', area)
    elif opcao == 'Q':
        lado = float(input('Lado do quadrado: '))
        area = lado**2
        print('A área do quadrado é', area)
    elif opcao == 'T':
        baseG = float(input('Base maior do trapézio: '))
        baseP = float(input('Base menor do trapézio: '))
        altura = float(input('Altura do trapézio: '))
        area = (baseG+baseP)/2 * altura
        print('A área do trapézio é', area)
    elif opcao != 'S':
        print('Opção inválida')


# Alterar o programa anterior separando cada um dos cálculos de área em diferentes funções. Essas funções não recebem nenhum valor como parâmetro e também não retornam valores.
def areaCirculo():
    raio = float(input('Raio do círculo: '))
    area = 3.14 * raio ** 2
    print('A área do círculo é', area)


def areaRetangulo():
    base = float(input('Base do retângulo: '))
    altura = float(input('Altura do retângulo: '))
    area = base * altura
    print('A área do retângulo é', area)


def areaQuadrado():
    lado = float(input('Lado do quadrado: '))
    area = lado**2
    print('A área do quadrado é', area)


def areaTrapezio():
    baseG = float(input('Base maior do trapézio: '))
    baseP = float(input('Base menor do trapézio: '))
    altura = float(input('Altura do trapézio: '))
    area = (baseG+baseP)/2 * altura
    print('A área do trapézio é', area)


opcao = ''
while opcao != 'S':
    print('\nCalcule a área de:')
    print('[C]írculo')
    print('[R]etângulo')
    print('[Q]uadrado')
    print('[T]rapézio')
    print('[S]air')
    opcao = input('Opção: ').upper()

    if opcao == 'C':
        areaCirculo()
    elif opcao == 'R':
        areaRetangulo()
    elif opcao == 'Q':
        areaQuadrado()
    elif opcao == 'T':
        areaTrapezio()
    elif opcao != 'S':
        print('Opção inválida')

# Alterar o programa anterior fazendo com qeu as funções recebam valores como parâmetros e retornem valores.


def areaCirculo(raio):
    area = 3.14 * raio ** 2
    return area


def areaRetangulo(base, altura):
    return base * altura

def areaQuadrado(lado):
    return lado**2

def areaTrapezio(baseG, baseP, altura):
    return (baseG+baseP)/2 * altura

opcao = ''
while opcao != 'S':
    print('\nCalcule a área de:')
    print('[C]írculo')
    print('[R]etângulo')
    print('[Q]uadrado')
    print('[T]rapézio')
    print('[S]air')
    opcao = input('Opção: ').upper()

    if opcao == 'C':
        raio = float(input('Raio do círculo: '))
        area = areaCirculo(raio)
        print('A área do círculo é', area)
    elif opcao == 'R':
        base = float(input('Base do retângulo: '))
        altura = float(input('Altura do retângulo: '))
        area = areaRetangulo(base, altura)
        print('A área do retângulo é', area)

    elif opcao == 'Q':
        lado = float(input('Lado do quadrado: '))
        area = areaQuadrado(lado)
        print('A área do quadrado é', area)

    elif opcao == 'T':
        baseG = float(input('Base maior do trapézio: '))
        baseP = float(input('Base menor do trapézio: '))
        altura = float(input('Altura do trapézio: '))
        area = areaTrapezio(baseG, baseP, altura)
        print('A área do trapézio é', area)

    elif opcao != 'S':
        print('Opção inválida')

# Ler data de nascimento de uma pessoa e exibir quantos dias ela já viveu.
dia = int(input('Que dia você nasceu? '))
mes = int(input('Que mês você nasceu? '))
ano = int(input('Que ano você nasceu? '))

dia_atual = int(input('Dia atual: '))
mes_atual = int(input('Mês atual: '))
ano_atual = int(input('Ano atual: '))


def diasCorridos(dia, mes, ano):
    # mês: 1,  2,  3,  4,  5,   6,   7,   8,   9,  10,  11,  12
    tabelaMeses = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    # Multiplicar por 365.25 leva em conta o ano bissexto, adicionando um quarto de dia extra para cada ano.
    dias = int(ano*365.25)
    dias += tabelaMeses[mes-1]
    if mes > 2 and ano % 4 == 0:
        dias += 1
    # adicionamos os dias do mês corrente
    dias += dia
    return dias


dias = diasCorridos(dia_atual, mes_atual, ano_atual) - \
    diasCorridos(dia, mes, ano)

print(f'Você tem {dias} de vida.')

# Outra forma:
def bissexto(ano):
    # Função para verificar se um ano é bissexto
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


def dias_do_mes(mes, ano):
    # Função para obter o número de dias em um mês
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if bissexto(ano) else 28

def dias_corridos(dia, mes, ano):
    # Função para calcular o total de dias decorridos
    total_dias = 0

    # Adicionar dias completos de anos inteiros
    for i in range(ano):
        total_dias += 366 if bissexto(i) else 365

    # Adicionar dias completos de meses inteiros
    for i in range(1, mes):
        total_dias += dias_do_mes(i, ano)

    # Adicionar dias do mês atual
    total_dias += dia

    return total_dias

# Obter a data de nascimento do usuário
dia_nascimento = int(input('Que dia você nasceu? '))
mes_nascimento = int(input('Que mês você nasceu? '))
ano_nascimento = int(input('Que ano você nasceu? '))

# Obter a data atual do usuário
dia_atual = int(input('Dia atual: '))
mes_atual = int(input('Mês atual: '))
ano_atual = int(input('Ano atual: '))

# Calcular dias corridos
dias = dias_corridos(dia_atual, mes_atual, ano_atual) - \
    dias_corridos(dia_nascimento, mes_nascimento, ano_nascimento)

print(f'Você tem {dias} dias de vida.')

# Desenvolva uma função somatorio(n) para calcular a soma de todos os valores ímpares de 1 até o número indicado.
n = int(input('Insira um número: '))

def somatorio(n):
    soma = 0
    for i in range(1, n+1, 2):
        soma += i
    return soma

print(somatorio(n))

# Desenvolva uma função sequencia(n) para calcular a sequência da potência de 2 até o valor informado.
n = int(input('Insira um número: '))
def sequencia(n):
    i = 1
    while 2 ** i <= n:
        print(2 ** i)
        i += 1

sequencia(n)

# Faça uma função chamada multiplos7(inicio,fim) que retorna a SOMA dos múltiplos de 7 entre um valor inicial e um valor final (inclusive).
def multiplos7(inicio, fim):
    soma = 0
    for numero in range(inicio, fim + 1):
        if numero % 7 == 0:
            soma += numero
    return soma

# Exemplo de uso:
inicio = int(input("Informe o valor inicial: "))
fim = int(input("Informe o valor final: "))

resultado = multiplos7(inicio, fim)
print(f"A soma dos múltiplos de 7 entre {inicio} e {fim} é {resultado}.")

# Somar os valores da diagonal principal de uma matriz quadrada.
import random
def criar_matriz (dim):
    matriz = [[random.randint(1,9) for j in range(dim)] for i in range(dim)]
    return matriz

def soma(matriz, dim):
    soma = 0
    for i in range(dim):
        soma += matriz[i][i]
    return soma

dim = int(input('Insira a dimensão da matriz: '))
matriz = criar_matriz(dim)
print(matriz)
print(soma(matriz, dim))

# # Outra forma
# matriz = [[1,2,3],[4,5,6],[7,8,9]]
# soma = 0
# for i in range(3):
#     soma = soma + matriz[i][i]
# print(soma)

# Substituir todos os números negativos de uma matriz por seu módulo
import random
def criar_matriz (dim):
    matriz = [[random.randint(-9,9) for j in range(dim)] for i in range(dim)]
    return matriz

def soma(matriz, dim):
    soma = 0
    for i in range(dim):
        soma += matriz[i][i]
    return soma

def modulo(matriz, dim):
    for i in range(dim):
        for j in range(dim):
            matriz[i][j] = abs(matriz[i][j])

dim = int(input('Insira a dimensão da matriz: '))
matriz = criar_matriz(dim)

print("Matriz original:")
print(matriz)

modulo(matriz, dim)
print("Matriz após aplicar o módulo:")
print(matriz)

print("Soma da diagonal principal após a modificação:")
print(soma(matriz, dim))

# Crie uma função que receba dois números e calcule a exponenciação (potência) do primeiro pelo segundo, ou seja, o primeiro número é a base e o segundo é o expoente. Nome da função: potencia().
def potencia(base, expoente):
    return base ** expoente

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = potencia(base, expoente)
print(f"{base} elevado a {expoente} é igual a {resultado}")

def potencia(base, expoente):
    resultado = base ** expoente
    return resultado

print(potencia(0, 1))

# Faça uma função troca() que recebe uma lista com dois valores e troca o conteúdo dos dois. Ou seja, o primeiro elemento da lista se transforma no segundo e o segundo se transforma no primeiro.
def troca(V):
    aux = V[0]
    V[0] = V[1]
    V[1] = aux

def troca(lista):
    if len(lista) == 2:
        temp = lista[0]
        lista[0] = lista[1]
        lista[1] = temp
    else:
        print("A lista deve conter exatamente dois elementos.")

# Exemplo de uso
minha_lista = random.sample(range(1, 100), 2)
print("Antes da troca:", minha_lista)

troca(minha_lista)
print("Depois da troca:", minha_lista)

# Faça uma função para calcular o fatorial de um número. Receba como parâmetro um número n e retorne como resposta n! Obs.: nome da função deve ser fatorial()
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def fatorial(n):
    resultado=1
    for num in range(1,n+1):
        resultado *= num
    return resultado

def fatorial(n):
    resultado=1
    num=1
    while num <= n:
        resultado *= num
        num += 1
    return resultado

numero = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")

# Crie uma função maior() que recebe três valores e retorna o maior dos três.
def maior(a, b, c):
    return max(a, b, c)

def maior(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c:
        return b
    return c

# Exemplo de uso
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

resultado = maior(num1, num2, num3)
print(f"O maior número é: {resultado}")