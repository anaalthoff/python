# pequena revisão
# Crie variáveis para armazenar:
# Nome do curso
# Número de alunos
# Média da turma
# Defina valores ficticios e imprima os valores

nome_curso = 'Tópicos Especiais'
num_alunos = 38
media_turma = 7.5
print(nome_curso)
print(num_alunos)
print(media_turma)

# 1 Operações Matemáticas
a = 10
b = 3

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("Divisão inteira:", a // b)
print("Resto:", a % b)
print("Potência:", a ** b)

# 2 Estrutura de Decisão
# Permite executar diferentes blocos de código dependendo de uma condição
nota = 7
if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# Crie um programa que:
# Receba uma idade
# Informe se a pessoa é:
# Criança (<12)
# Adolescente (12–17)
# Adulto (18+)
idade = int(input('Digite sua idade: '))
if idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
else:
    print('Adulto')

# 3 Estrutura de Repetição
# 3.1. For
# Usado para percorrer sequências

for i in range(5):
    print(i)

# 3.2. While
# Executa enquanto a condição for verdadeira

contador = 0

while contador < 5:
    print(contador)
    contador += 1

# Crie um programa com um loop que imprima os números de pares de 1 a 10
for i in range(2, 11, 2):
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

numero = 1
while numero <= 10:
    if numero % 2 == 0:
        print(numero)
    numero += 1

# 4 Listas
# Estrutura de dados que armazena múltiplos valores.

frutas = ["maçã", "banana", "uva"]

# Acessando elementos:
print(frutas[0])

# Adicionando elementos:
frutas.append("laranja")

# Percorrendo lista:
for fruta in frutas:
    print(fruta)

# Crie um programa com uma lista de 5 palavras relacionadas à tecnologia.
# Imprima todas(utilize estrutura de repetição)
# Conte quantos elementos existem
# Adicione mais um item a lista

palavras_tecnologia = ['programação',
                       'desenvolvimento', 'IA', 'linguagem', 'raciocínio']
for palavra in palavras_tecnologia:
    print(palavra)

# Contando quantos elementos existem
print("\nQuantidade de elementos:", len(palavras_tecnologia))

# Adicionando mais um item à lista
palavras_tecnologia.append("Banco de Dados")

print("\nLista atualizada:")
for item in palavras_tecnologia:
    print(item)

print("\nNova quantidade de elementos:", len(palavras_tecnologia))

# 5 Funções
# Funções organizam código reutilizável.

# Sintaxe:


def nome_funcao(parametros):
    return resultado

# Exemplo:


def soma(a, b):
    return a + b


resultado = soma(3, 5)
print(resultado)

# Crie um programa que utiliza uma função que:
# Receba uma lista de números
# Retorne a média


def calcular_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


# Lista de exemplo
numeros = [10, 8, 7, 9, 6]

# Chamando a função
media = calcular_media(numeros)

print("Lista de números:", numeros)
print("Média:", media)

# Ler dois números quaisquer, calcular a soma, mostrar os números lidos e o resultado da soma
num1 = float(input())
num2 = float(input())

sum = num1 + num2
print(num1, num2, sum)

# Ler dois números reais. Multiplicar o primeiro por 4 e o segundo por 0,6. Calcular a média aritmética dos resultados obtidos. Imprimir os valores lidos, os calculados e a média aritmética.
num1 = float(input())
num2 = float(input())

num3 = num1 * 4
num4 = num2 * 0.6

media_aritmetica = (num3 + num4) / 2

print(num1, num2, num3, num4, media_aritmetica)

# Faça um programa em Python para calcular a área de uma elipse. O usuário entra com o valor do raio e o programa informa a área da elipse com o seguinte texto: "Área da elipse é:<n>" (sem aspas, onde <n> é o valor calculado). Considere o valor de pi como 3.14.
raio_maior = float(input())
raio_menor = float(input())
area_elipse = raio_maior * raio_menor * 3.14
print("Área da elipse é:", area_elipse)

# Faça um programa em Python para ler dois valores quaisquer (real/float) para as variáveis A e B, efetuando a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresente ao final os valores trocados.
# Obs.: sim, se trocar a ordem da do print sem fazer nada vai funcionar. Mas NÃO é o que pede o exercício, seu esperto. ;-)

num1 = float(input())
num2 = float(input())
temp = num1
num1 = num2
num2 = temp

print(num1)
print(num2)

# Faça um programa em Python que calcule a área de um triângulo.
# Leia dois números reais, o primeiro é a base e o segundo a altura.
# Calcule e mostre a área do triângulo.
# O programa mostra a área do triângulo cm o seguinte texto: "Área da triângulo é: <area>" (sem aspas, onde <area> é o valor calculado).
base = float(input())
altura = float(input())
area = (base*altura)/2
print("Área do triângulo é:", area)

# Faça um programa em Python para ler dois números reais quaisquer, calcular o produto, mostrar os números lidos e o resultado do produto.
# O programa mostra a área do triângulo cm o seguinte texto: "<numero1> vezes <numero2> é igual a <produto>" (sem aspas, onde <numero1> é o primeiro número, <numero2> o segundo e <produto> o valor calculado).
num1 = float(input())
num2 = float(input())
produto = num1*num2
print(num1, "vezes", num2, "é igual a", produto)

# Faça um programa em Python para calcular a média ponderada de duas notas de um aluno. A primeira nota tem peso 3 e a segunda peso 2. Imprimir as notas lidas e a média calculada.
# O programa mostra a média seguinte texto: "A média é: <media>" (sem aspas, onde <media> é o valor calculado).
nota1 = float(input())
nota2 = float(input())
media_ponderada = ((nota1 * 3) + (nota2 * 2))/5
print("A média é:", media_ponderada)

# Faça um programa em Python que calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros). A entrada é um valor inteiro representando a distância total percorrida (em Km), e um valor real representando o total de combustível gasto. Apresente o valor que representa o consumo médio do automóvel, seguido da mensagem "km/l".
# O programa mostra o consumo com o seguinte texto: "<consumo> km/l" (sem aspas, onde <consumo> é o valor calculado).
distancia = int(input())
combustivel = int(input())
consumo = distancia/combustivel
print(consumo, "km/l")

# Faça um programa em Python que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R^3. Considere (atribua) para pi o valor 3.14. Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro inteiro. Se não conseguir calcular o cubo de R utilize R * R * R.
# O programa mostra o volume da esfera com o seguinte texto: "O volume é: <volume>" (sem aspas, onde <volume> é o valor calculado).
raio = float(input())
pi = 3.14
volume = (4/3.0) * pi * raio ** 3
print("O volume é:", volume)

# Leia dois números quaisquer e dividir o primeiro pelo segundo (evitando divisão por zero). Caso o segundo valor seja zero, informe como resposta "Erro: divisão por zero!".
num1 = float(input())
num2 = float(input())

if num2 == 0:
    print("Erro: divisão por zero!")
else:
    divisao = num1/num2
    print(divisao)

# Ler dois números inteiros e exibir o maior deles. Escreve o valor mesmo que o usuário tenha informado números iguais.
num1 = float(input())
num2 = float(input())

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print(num1)

# Ler um número inteiro e imprimir se ele é par ou ímpar. Use como saída as strings "Par" e "Ímpar".
num1 = float(input())
if num1 % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# Ler três números inteiros e exibir o maior deles. Exiba apenas o valor do maior.
num1 = int(input())
num2 = int(input())
num3 = int(input())

maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print(maior)

# Faça um programa que calcule o IMC de uma pessoa (IMC = massa em kg / altura em metros elevado ao quadrado) e informe a sua classificação segundo a tabela a seguir, obtida na Wikipédia:

#       IMC        	Classificação
#       < 18,5      	Abaixo do peso
# [18,5 - 25)	Saudável
# [25 – 30)	Peso em excesso
# [30 – 35)	Obesidade Grau I
# [35 – 40)	Obesidade Grau II (severa)
# >= 40	Obesidade Grau III (mórbida)

massa = float(input())
altura = float(input())
imc = massa / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Peso em excesso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")

# Ler um número inteiro e imprimir a seguinte estrutura:

# *
# **
# ***
# ****
# *****
# ******

# Obs.: o usuário entra com um valor que é a altura da estrutura (número de linhas) e a cada linha, são exibidos tantos asteriscos quanto o número da linha. Para desenhar três asteriscos, use: print('*'*3)

num = int(input())
for i in range(1, num + 1):
    print("*" * i)

# Calcular a média das notas de uma turma. Entrada do programa: o número de alunos da turma e na sequência a nota de cada um dos alunos. A média deve ser mostrada com uma casa decimal.
alunos = int(input())
soma = 0

for i in range(alunos):
    nota = float(input())
    soma += nota

media = soma/alunos
print(f"{media:.1f}")

# Ler dois números inteiros. Se os números forem iguais, imprimir a mensagem "Números iguais" e encerrar a execução. Caso contrário, imprimir o de maior valor.
num1 = int(input())
num2 = int(input())

if num1 == num2:
    print("Números iguais")
elif num1 > num2:
    print(num1)
else:
    print(num2)

# Faça um programa que leia dois números inteiros. O primeiro é o valor inicial de um contador, e o segundo é o valor final do contador (garanta que o valor inicial fornecido é inferior ao valor final, independente dos valores digitados pelo usuário). Escreva na tela uma contagem que comece no primeiro número lido, escreva os números seguintes colocando apenas um número em cada nova linha da tela, até chegar ao valor final indicado.
inicial = int(input())
final = int(input())

while inicial > final:
    inicial, final = final, inicial

for i in range(inicial, final+1):
    print(i)

# Faça um programa para calcular o fatorial de um número. A entrada do  programa é um valor inteiro e a saída mostra o número e seu fatorial (5! = 120).
num = int(input())
fatorial = 1

for i in range(1, num + 1):
    fatorial = fatorial * i
    i = i + 1

print(f'{num}! = {fatorial}')

# Crie um programa em Python para ler como informação de entrada um número inteiro. O programa deve somar todos os valores de 1 até o valor informado. Por exemplo, se o usuário entrar com o número 50, o programa deverá somar todos os inteiros de 1 até 50 (1+2+3+...+49+50). Veja a resposta abaixo e corrija o algoritmo.
# entrada de dados
n = int(input())
soma = 0

# conta de 1 até n e soma todos os valores
i = 1
while i <= n:
    soma = soma + i
    i = i + 1

# exibe o resultado da soma
print(soma)

# Faça um programa em Python para fazer a média de vários valores indicados pelo usuário. O usuário entra primeiramente com a quantidade de valores e em seguida a sequência de valores (tipo float). A saída do programa é a média de todos os valores.
qtd = int(input())
soma = 0

for i in range(qtd):
    valores = float(input())
    soma += valores

media = soma/qtd
print(media)

# Escreva um algoritmo que permita a leitura de 7 números inteiros. Gere um vetor com os mesmos valores digitados, mas de maneira invertida, ou seja, o primeiro número lido ficará na última posição do vetor. Exiba o vetor ao final colocando um número a cada linha.

vetor = []

for i in range(7):
    num = int(input())
    vetor.append(num)

for i in range(6, -1, -1):
    print(vetor[i])

# Crie um programa em Python para ler dois vetores de 15 posições de inteiros cada e mostre a interseção dos vetores. Primeiro faça a leitura dos 15 valores inteiros para o primeiro vetor e depois os 15 valores do segundo. Para facilitar, considere que os valores não se repetem dentro do mesmo vetor. Lembrando que intersecção são elementos repetidos em ambos sem repetição (observe que os valores iguais normalmente não estarão na mesma posição).

vetor1 = []
vetor2 = []

for i in range(15):
    num = int(input())
    if num not in vetor1:
        vetor1.append(num)

for j in range(15):
    num = int(input())
    if num not in vetor2:
        vetor2.append(num)

for num in vetor1:
    if num in vetor2:
        print(num)

# Faça um algoritmo que leia um vetor de 30 elementos inteiros e exiba o mesmo em ordem crescente. Imprima (exiba) um valor por linha.
vetor = []

for i in range(30):
    num = int(input())
    vetor.append(num)

vetor.sort()

for num in vetor:
    print(num)

# Fazer um programa para ler um vetor de 10 números inteiros, somar estes valores e exibir a soma.
vetor = []

for i in range(10):
    num = int(input())
    vetor.append(num)

soma = sum(vetor)

print(soma)

# Qual a saída do seguinte programa?
lista = [1, 2, 3, 4, 5]

valor = 1
for i in range(5):
    valor = valor * lista[i]

# Output
print(valor)
