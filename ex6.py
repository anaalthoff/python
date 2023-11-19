# iteração
notas = [8.0, 5.5, 1.5]
for i in range(3):
    print(notas[i])

# deve-se informar o tamanho do array. caso não saiba, pode criar um array vazio a adicioanr os valores posteriormente usado append. Mas se já sabe, melhor especificar para não precisar uar appens

notas = []
notas.append(float(input('Primeira nota: ')))
notas.append(float(input('Segunda nota: ')))
notas.append(float(input('Terceira nota: ')))

for i in range(len(notas)):
    print(notas[i])

# outra forma de iterar
notas = []
notas.append(float(input('Primeira nota: ')))
notas.append(float(input('Segunda nota: ')))
notas.append(float(input('Terceira nota: ')))

for i in notas:
    print(i)

# possível concatenar listas com '+'
# '*' repete n vezes os elementos que estão na lista
n = int(input('Qual o tamanho da lista: '))
lista = [0]*n
for i in range(n):
    lista[i] = i+1
print(lista)

# Ler um um vetor de 8 números inteiros
vetor = []
for i in range(8):
    num = (int(input('Insira 8 valores: ')))
    vetor.append(num)
print('Valores lidos: ')
print(vetor)

# Outra forma:
vetor = [0]*8
for i in range(8):
    num = (int(input('Insira 8 valores: ')))
    vetor[i] = num
print('Valores lidos: ')
print(vetor)

# Altere a ordem dos números do exercício anterior
vetor = [0]*8
for i in range(8):
    vetor[i] = int(input('Insira 8 valores: '))
vetor.reverse()
print(vetor)

# Outra forma:
vetor = [0]*8
for i in range(8):
    vetor[i] = int(input('Insira 8 valores: '))
for i in range(7, -1, -1):
    # for i in range(-1,-9,-1):
    print(vetor[i])

# Leia 8 números, mostre a soma de seus elementos e apesente quais são positivos
vetor = [0]*8
for i in range(8):
    vetor[i] = int(input('Insira 8 valores: '))

soma = 0
positivos = 0
for i in range(8):
    soma = soma + vetor[i]
    if vetor[i] >= 0:
        positivos = positivos + 1

print(vetor)
print('Resultado da soma:', soma)
print('A quantidade de números positivos é:', positivos)

# Escrever um algoritmo que leia dois vetores de 5 posições e calcule o produto escalar entre ambos vetores escrevendo a resposta
# (Ax*Bx) + (Ay*By) + ...
v1 = [0.0]*5
v2 = [0.0]*5

print('Insira 5 valores para o 1º vetor: ')
for i in range(5):
    v1[i] = float(input())

print('Insira 5 valores para o 2º vetor: ')
for i in range(5):
    v2[i] = float(input())

pe = 0.0
for i in range(5):
    pe = pe + v1[i]*v2[i]

print(v1)
print(v2)
print('Produto escalar: ', pe)

# Ler nome e nota de uma turma de até 30 alunos
# Exiba uma lista com o nome dos alunos que tiveram nota acima de 7

nomes = []
notas = []

for i in range(3):
    nomes.append(input('Nome do aluno:'))
    notas.append(float(input('Nota do aluno:')))
print(nomes)
print(notas)

for i in range(3):
    if notas[i] >= 7:
        print(nomes[i])

# Faça um programa para preencher com leitura um vetor de 5 posições e informa a posição em que um valor x (também lido do teclado) está no vetor. Caso o valor não seja encontrado, o programa deve imprimir o valor -1
vetor = [0]*5

print('Entre com 5 valores: ')
for i in range(5):
    vetor[i] = int(input())

x = int(input('Entre com o valor a pesquisar no vetor: '))

posicao = -1
for i in range(5):
    if vetor[i] == x:
        posicao = i
        break

print(x, 'está na posição', posicao)

# Ler dois vetores de 15 posições de inteiros cada e mostrar a interseção dos vetores
v1 = [0] * 15
v2 = [0] * 15

inter = []
for i in range(15):
    v1[i] = int(input())

for i in range(15):
    v2[i] = int(input())

for elemento in v1:
    if elemento in v2:
        inter.append(elemento)

for elemento in inter:
    # se deixar apenas print(elemento), virá como array, uma lista
    print(elemento)

# Ler um vetor de 30 elementos inteiros e exibi-lo em ordem crescente. Imprimir um valor por linha.
vetor = []
for i in range(30):
    elemento = int(input())
    vetor.append(elemento)

vetor_ordenado = sorted(vetor)

for elemento in vetor_ordenado:
    print(elemento)

# Ler um vetor de 10 números inteiros, somar estes valores e exibir a soma.
vetor = []
soma = 0
for i in range(10):
    elemento = int(input())
    soma = soma + elemento
print(soma)
