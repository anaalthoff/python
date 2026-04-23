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

palavras_tecnologia = ['programação', 'desenvolvimento', 'IA', 'linguagem', 'raciocínio']
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