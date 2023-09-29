# Repetição
# Conte de 1 a 100
numero = 1
while numero <= 100:
    print(numero)
    numero = numero + 1

# Imprima os números pares de 100 a 200
n1 = 100
while n1 <=200:
    print(n1)
    n1 = n1 + 2

# Outra forma:
num = 100
while num<= 200:
    if num %2 == 00:
        print(num)
    num = num + 1

# Imprima a quantidade de números pares de 100 a 200
pares = 0
i = 100
while i <= 200:
    if i %2 == 0:
        pares = pares + 1
    i = i + 1
print('São', pares, 'números pares de 100 a 200.')

# Imprima a quantidade de números pares entre dois números
n2 = int(input('Insira um número: '))
n3 = int(input('Insira outro número: '))
pares = 0
i = n2
while i <= n3:
    if i %2 == 0:
        pares = pares + 1
    i = i + 1
print('São', pares, 'números pares de',n2,'a', n3)

# Faixa de valores apenas com valor final
for variavel in range(6):
    print(variavel)

# Faixa de valores com valor inicial e final
for variavel in range(1,6):
    print(variavel)

# Faixa de valores com valor inicial, final e incremento
for variavel in range(2,10,2):
    print(variavel)

# Imprima a quantidade de números pares entre dois números
n2 = int(input('Insira um número: '))
n3 = int(input('Insira outro número: '))
pares = 0
cont = n2
for cont in range (n2, n3):
    if cont %2 == 0:
        pares = pares + 1
print('São', pares, 'númerps pares de',n2,'a', n3)

# Imprima a quantidade de números pares de 100 a 200
for num in range (100,201):
    if num %2 == 0:
        print('São', pares, 'números pares de 100 a 200.')

# Imprima os números pares de 2 em 2 de 100 a 200
for num in range(100, 201, 2):
    print(num)

# Calcular o fatorial de um número informado pelo usuário
n = int(input('Insira um número: '))
i = 1 
fatorial = 1
while i <= n:
    fatorial = fatorial * i
    i = i + 1
print(f'{n}! = {fatorial}')

# Com FOR
n = int(input('Insira um número: '))
fatorial = 1
for i in range(1, n+1):
    fatorial = fatorial * i
    i = i + 1
print(f'{n}! = {fatorial}')

# Montar a tabela de multiplicação de números de 1 a 10(ex: 1 x 1 = 1, 1 x 2 = 2, etc)
n = int(input('Escreva um número de 1 a 10: '))
i = 1
while i <= 10:
    print(n, 'x', i,'=',n*i)
    i = i+1

# Com FOR
for n in range(1,11):
    print('\nTabuada do', n)
    for i in range(1,11):
        print(n, 'x', i,'=',n*i)

# Determinar o número de dígitos de um número inteiro positivo informado
numero = int(input('Escreva um número inteiro: '))
n = numero
qtd = 1
while n // 10 > 0:
    qtd = qtd + 1
    n = n // 10
print(numero, 'tem', qtd, 'dígitos.')

# Faça um programa para calcular a série de Fibonacci para um número informado
n = int(input('Entre com o número de termos para fazer a série Fibonacci: '))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)

# Com FOR
n = int(input('Entre com o número de termos para fazer a série Fibonacci: '))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    for count in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)

# Com WHILE
n = int(input('Entre com o número de termos para fazer a série Fibonacci: '))
print(0)
if n>0:
    print(1)
n_2 = 0
n_1 = 1
while n > 1:
    fib = n_1 + n_2
    print(fib)
    n = n - 1
    n_2 = n_1
    n_1 = fib

# Ler um número inteiro e imprimir a seguinte estrutura:

# *
# **
# ***
# ****
# *****
# ******

# Obs.: o usuário entra com um valor que é a altura da estrutura (número de linhas) e a cada linha, são exibidos tantos asteriscos quanto o número da linha. Para desenhar três asteriscos, use: print('*'*3)

altura = int(input('Insira o número de linhas: '))
# Em Python, o intervalo gerado por range(início, fim) é inclusivo no início e exclusivo no fim. Isso significa que o valor no fim não será incluído no intervalo
for i in range(1, altura + 1):
    print('*' * i)

# Com WHILE
altura = int(input('Insira o número de linhas: '))
linha = 1

while linha <= altura:
    print('*' * linha)
    linha += 1

# Calcular a média das notas de uma turma. Entrada do programa: o número de alunos da turma e na sequência as notas de cada um dos alunos.
alunos = int(input('Insira o número de alunos: '))
soma = 0
# A variável _ é comumente usada em Python quando o valor de uma variável não é necessário dentro do loop
for _ in range(alunos):
# for linha in range(0,num):
    nota = float(input('Insira a nota do aluno: '))
    soma += nota

media = soma/alunos
print(f'A média das notas é: {media:.1f}')
# print("A média das notas é: {:.1f}".format(media))

# Com WHILE
alunos = int(input('Insira o número de alunos: '))

soma = 0
cont = 0

while cont < alunos:
    # O f na frente da string indica uma f-string em Python, uma maneira de formatar strings, permitindo a incorporação de expressões e variáveis diretamente na string
    nota = float(input(f'Insira a nota do aluno {cont + 1}: '))
    soma += nota
    cont += 1

media = soma/alunos
print("A média das notas é: %.1f" % media)

# Ler dois números inteiros. Se os números forem iguais, imprimir a mensagem "Números iguais" e encerrar a execução. Caso contrário, imprimir o de maior valor.
n_1 = int(input('Insira um número: '))
n_2 = int(input('Insira outro número: '))
if n_1 == n_2:
    print('Números iguais')
elif n_1 > n_2:
    print(n_1,'é maior que', n_2)
else:
    print(n_2,'é maior que', n_1)

# Faça um programa que leia dois números inteiros. O primeiro é o valor inicial de um contador, e o segundo é o valor final do contador (garanta que o valor inicial fornecido é inferior ao valor final, independente dos valores digitados pelo usuário). Escreva na tela uma contagem que comece no primeiro número lido, escreva os números seguintes colocando apenas um número em cada nova linha da tela, até chegar ao valor final indicado.
# Solicita os números do usuário e garante que o valor inicial é inferior ao valor final
valor_inicial = int(input('Digite o valor inicial do contador: '))
valor_final = int(input('Digite o valor final do contador (deve ser maior que o valor inicial): '))

while valor_inicial >= valor_final:
    print('O valor inicial deve ser menor que o valor final.')
    valor_inicial = int(input('Digite o valor inicial do contador: '))
    valor_final = int(input('Digite o valor final do contador (deve ser maior que o valor inicial): '))

for i in range(valor_inicial, valor_final + 1):
    print(i)

# Outra forma
n1 = int(input())
n2 = int(input())

# troca se primeiro maior que segundo valor
if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux

# conta de n1 a n2 e exibe linha a linha
for n in range(n1,n2+1):
    print(n)

# Outra forma
n1 = int(input())
n2 = int(input())

# troca se primeiro maior que segundo valor
if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux

# conta de n1 a n2 e exibe linha a linha
n = n1
while n<=n2:
    print(n)
    n = n + 1

# Ler como informação de entrada um número inteiro. O programa deve somar todos os valores de 1 até o valor informado.
n = int(input('Digite um número: '))

soma = 0
i = 1
while i <= n:
    soma = soma + i
    i = i + 1

print(f"A soma de 1 até {n} é: {soma}")

# Fazer a média de vários valores indicados pelo usuário
valores = int(input('Insira a quantidade de valores: '))
soma = 0

for _ in range(valores):
    valor = float(input('Digite um valor: '))
    soma += valor

media = soma / valores
print(f'A média dos {valores} valores é: {media:.2f}')
