# Matrizes - vetor com mais de uma dimensão, lista dentro de lista
# valor = matriz[2][3] -> significa que quer pegar a terceira linha da quarta coluna
# matriz [1][0] = 5 -> primeiro elemento da segunda linha recebe valor 5

# Criar um vetor (matriz unidimensional) de 8 números inteiros, composto de múltiplos de 3 inicianod pelo valor 15.
import random
vetor = [0]*8
for i in range(8):
    vetor[i] = 15 + (i*3)
print(vetor)

# Outra forma

vetor = []
for i in range(8):
    vetor.append(15 + i * 3)

print(vetor)

# Dada uma matriz 3X3, armazenar em cada posição da matriz a soma dos valores da linha e da coluna que definem a posição. Exibir a matriz.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        matriz[i][j] = i+j

# faz com que alinhe ao lado
# print (matriz)

# alinha uma linha abaixo da outra
for i in range(3):
    print(matriz[i])

# Compreensão - forma de modificar e filtrar listas em Python
# Mais rápidas de executar que os laços for e não precisam da instrução append
# Sintaxe -> [<expressão> for <item> in <lista>]
# expressão - qualquer sentença que retorne um valor
# item - representa cada elemento da lista a ser criada
# lista - a lista a ser criada
# NumPy - biblioteca para realizar operações em arrays multidimensionais

# Exemplo de uma lista tradicional:
lista = []
for i in range(1, 10):
    lista.append(i * 10)
print(lista)

# Possível reescrever da seguinte forma:
lista = [i*10 for i in range(1, 10)]
print(lista)

# Com condições:
lista = [i*10 for i in range(1, 10) if i % 2 == 0]
print(lista)


# Com matriz:
matriz = [[i+j for j in range(3)] for i in range(1, 10, 3)]
print(matriz)

# Criar uma matriz identidade de tamanho 5x5:
matriz = [[1 if i == j else 0 for j in range(5)]for i in range(5)]
for i in range(5):
    print(matriz[i])

# Fazer um programa que preencha uma matriz 20x3 com notas de vinte alunos em 3 provas (valores de 0 a 10). Deve mostrar em que posição aparecem as menores notas para: prova 1 , prova 2 e prova 3. Exibir posição e nota.

# define que a maioria receba 6, com variação em torno de 2, mas pode ocorrer de vir numero negativo e maior que 10 tbm
matriz = [[random.normalvariate(6, 2) for j in range(3)] for i in range(20)]

# caso nota negativa ou maior que 10
for i in range(20):
    for j in range(3):
        # Corrige notas negativas
        if matriz[i][j] < 0:
            matriz[i][j] = 0
        # Corrige notas maiores que 10
        elif matriz[i][j] > 10:
            matriz[i][j] = 10


# buscando a menor nota. esses valores serão substituídos, por isso não importa muito quais são
min_nota1 = min_nota2 = min_nota3 = 11
pos_nota1 = pos_nota2 = pos_nota3 = -1

for i in range(20):
    if (matriz[i][0] < min_nota1):
        min_nota1 = matriz[i][0]
        pos_nota1 = i

    if (matriz[i][1] < min_nota2):
        min_nota2 = matriz[i][0]
        pos_nota2 = i

    if (matriz[i][2] < min_nota3):
        min_nota3 = matriz[i][0]
        pos_nota3 = i

# outra forma de buscar a menor nota:
notas1 = [x[0] for x in matriz]
notas2 = [x[1] for x in matriz]
notas3 = [x[2] for x in matriz]

min_nota1 = min(notas1)
min_nota2 = min(notas2)
min_nota3 = min(notas3)

pos_nota1 = notas1.index(min_nota1)
pos_nota2 = notas2.index(min_nota2)
pos_nota3 = notas3.index(min_nota3)

print(f'Posição da menor nota 1 é {pos_nota1} e nota mínima é {min_nota1:2.2}')
print(f'Posição da menor nota 2 é {pos_nota2} e nota mínima é {min_nota2:2.2}')
print(f'Posição da menor nota 3 é {pos_nota3} e nota mínima é {min_nota3:2.2}')

print('\nMatriz:')
for i in matriz:
    # 4 é a largura total do campo, incluindo espaços à esquerda do número, .1 indica que haverá 1 casa decimal, f significa ponto flutuante.
    print('%4.1f %4.1f %4.1f' % (i[0], i[1], i[2]))

# Fazer um programa que gera uma matriz 7x7 preenchida com valores aleatórios de 0 a 100. Escrever a matriz na tela e os seguintes valores:
# posição (linha e coluna) onde está o maior valor, quantas vezes o maior valor aparece (pode repetir), posição onde está o menor valor, quanats vezes o menor valor aparece
matriz = [[random.randint(0,100) for j in range(7)]for i in range(7)]

print('Matriz:')
for i in matriz:
    print(i)

# colocar menor que 0
# Valor:
maior = -1
# Posição:
maior_i = maior_j = -1

# Valor:
menor = 101
# Posição:
menor_i = menor_j = -1

cont_maior = cont_menor = 0

for i in range(7):
    for j in range(7):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            maior_i = i
            maior_j = j

        if matriz[i][j] < menor:
            menor = matriz[i][j]
            menor_i = i
            menor_j = j

for i in range(7):
    for j in range(7):
        if matriz[i][j] == maior:
            cont_maior += 1

        if matriz[i][j] == menor:
            cont_menor += 1

print(f'Maior é {maior}, aparece na posição [{maior_i}][{maior_j}] e aparece {cont_maior} vezes.')
print(f'Menor é {menor}, aparece na posição [{menor_i}][{menor_j}] e aparece {cont_menor} vezes.')

# Multiplicaçaõ entre dois valores das matrizes
matriz = [[1,2,3],[7,8,9],[5,6,7]]
valor = matriz[1][1] *matriz[2][2]
print(valor)

# Criar uma matriz 5x5 preenchida com uma sequência numérica
matriz = [[j+(5*i) for j in range(5)] for i in range(5)]
print(matriz)

# Outra forma: matriz = [[i + j*5 for i in range(5)] for j in range(5)]

# Somar todos os elementos da matriz do exercício anterior e calcular a média dos valores. Exibir ao final uma linha com a soma dos valores (valor inteiro) e outra linha com a média dos valores da matriz com uma casa decimal.

soma = 0
for i in range(5):
   soma = soma + sum(matriz[i])
print(soma)
print("%.1f" % (soma/25.0))

# Outra forma:
soma = 0
for i in range(5):
   for j in range(5):
      soma = soma + matriz[i][j]
print(soma)
media = soma/25.0
print("%.1f" % (media))

# Outra forma:
# for linha in matriz: itera sobre cada linha na matriz. Para cada linha, a variável linha contém os elementos dessa linha.
# sum(linha) for linha in matriz: para cada linha da matriz, usa-se a função sum para somar todos os elementos da linha.
# sum(sum(linha) for linha in matriz): soma todos esses resultados.
soma_total = sum(sum(linha) for linha in matriz)

# Calcular a média dos valores
# len(matriz[0]: retorna o número de elementos na primeira linha da matriz, basicamente representa o número de colunas na matriz.
quantidade_elementos = len(matriz) * len(matriz[0])
media = soma_total / quantidade_elementos

# Criar uma matriz 5x4 preenchendo em cada célula a multiplicação dos índices da matriz. Por exemplo, na posição [2][3] será colocado o valor 6 (2x3);
# O programa deve ler 12 valores inteiros, representando 6 posições (e 3 pares de posições). A cada quatro valores, representando duas posições na matriz, faça a troca dos valores na matriz;
# Faça as três trocas (para os 3 pares de posições);
# Mostre a matriz ao final usando print(matriz).
# Criar uma matriz 5x4 preenchendo em cada célula a multiplicação dos índices
matriz = [[i * j for j in range(4)] for i in range(5)]

# Ler 12 valores inteiros
for i in range(3):
    i1 = int(input())
    j1 = int(input())
    i2 = int(input())
    j2 = int(input())

    # Trocar os valores nas posições indicadas
    matriz[i1][j1], matriz[i2][j2] = matriz[i2][j2], matriz[i1][j1]

# Mostrar a matriz ao final
print(matriz)

# Ler dois valores inteiros L e C.
# Crie uma matriz de inteiros com dimensão LxC;
# Preencha a matriz com valores informados pelo usuário. Faça a leitura de cada um dos valores da matriz;
# Exiba a matriz ao final: print(matriz).
# Ler dois valores inteiros L e C
L = int(input("Digite o número de linhas (L): "))
C = int(input("Digite o número de colunas (C): "))

# Criar uma matriz de inteiros com dimensão LxC
matriz = [[0] * C for i in range(L)]

# Preencher a matriz com valores informados pelo usuário
for i in range(L):
    for j in range(C):
        matriz[i][j] = int(input(f'Digite o valor para a posição [{i}][{j}]: '))

# Exibir a matriz ao final
print(matriz)

# Outra forma:
matriz = [[i*j for j in range(4)] for i in range(5)]
for i in range(3):
    l1 = int(input())
    c1 = int(input())
    l2 = int(input())
    c2 = int(input())
    aux = matriz[l1][c1]
    matriz[l1][c1] = matriz[l2][c2]
    matriz[l2][c2] = aux
print(matriz)