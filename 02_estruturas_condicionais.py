# Operadores lógicos: utilizar not (negação), and (E) e or (OU)
# Dada a idade de uma pessoa, exiba se essa pessoa está apta a votar

idade = int(input('Escreva sua idade: '))
if idade >= 16:
    print('Apto a votar')
# pode escrever else:
print('Não está apto a votar')

# Soma entre dois números
op = input('Deseja somar? (S/N)')
if op == "S":
    x = int(input("Digite um número: "))
    y = int(input("Digite um número: "))
    resultado = x + y
    print("O resultado da some é" , resultado)
else: 
    print("Até a próxima")

# Soma ou multiplicação de dois números
pergunta = input('Deseja somar (S) ou multiplicar (M)?')
if pergunta != 'S' and pergunta != 'M':
    print('Opção inválida')
else:
    z = int(input("Digite um número: "))
    w = int(input("Digite um número: "))
    if pergunta == 'S':
        soma = z + w
        print('O resultado da soma é', soma)
    else:
        multiplicacao = z * w
        print('O resultado da multiplicação é', multiplicacao)

# Verificar se aluno está aprovado
nota = float(input('Isira a nota do aluno: '))
if nota >= 7:
    print('Aprovado')
elif nota >= 1.7:
    print('Em recuperação')
else:
    print('Reprovado')

# Verificar se números são iguais
a = int(input('Insira um número: '))
b = int(input('Insira um número: '))
c = int(input('Insira um número: '))
if a == b == c:
    print('Iguais.')
else:
    print('Não iguais')

# Verificar se aluno está aprovado a partir de 3 notas
prova1 = float(input('Insira a nota da primeira prova do(a) aluno(a): '))
prova2 = float(input('Insira a nota da segunda prova do(a) aluno(a): '))
prova3 = float(input('Insira a nota da terceira prova do(a) aluno(a): '))
mediaAluno = (prova1+prova2+prova3)/3
if mediaAluno >= 6 and prova1 >= 5 and prova2 >= 5 and prova3 >= 5:
    print('Aprovado')
else:
    print('Reprovado')

# Ler ano e verificar se ele é bissexto, par ou ímpar
ano = int(input('Insira um ano: '))
if ano%4 == 0:
    print('Ano', ano, 'é bissexto e par.')
elif ano%4 != 0 and ano%2 == 0:
    print('Ano', ano, 'é par, mas não bissexto.')
else:
    print('Ano', ano, 'é ímpar.')

# Leia dois números quaisquer e divida o primeiro pelo segundo (evitando divisão por zero). Caso o segundo valor seja zero, informe como resposta "Erro: divisão por zero!".
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
if n2 == 0:
    print('Erro: divisão por zero!')
else:
    print(n1/n2)

# Ler dois números inteiros e exibir o maior deles. Escrever o valor mesmo que o usuário tenha informado números iguais.
n3 = int(input('Insira um número: '))
n4 = int(input('Insira outro número: '))
if n3 > n4:
    print('O número', n3, 'é o maior.')
elif n4 > n3:
    print('O número ', n4, ' é o maior.')
else:
    print('Os dois números são iguais.')

# Ler um número inteiro e imprimir se ele é par ou ímpar. Use como saída as strings "Par" e "Ímpar".
n5 = int(input('Insira um número: '))
if n5%2==0:
    print('O número é par.')
else:
    print('O número é ímpar.')

# Ler três números inteiros e exibir o maior deles. Exiba apenas o valor do maior.
n6 = int(input('Insira um número: '))
n7 = int(input('Insira outro número: '))
n8 = int(input('Insira outro número: '))
if n6 > n7 and n6 > n8:
    print('O maior número entre os 3 é o', n6)
elif n7 > n6 and n7 > n8:
    print('O maior número entre os 3 é o', n7)
else:
    print('O maior número entre os 3 é o',n8)

# Faça um programa que calcule o IMC de uma pessoa e informe a sua classificação
peso = float(input('Insira o peso em kg (ex: 70): '))
altura = float(input('Insira a altura em metros (ex: 1.73): '))
imc = peso/(altura*altura)
if imc >= 40:
    print('Obesidade Grau III')
elif imc >= 35:
    print('Obesidade Grau II')
elif imc >= 30:
    print('Obesidade Grau I')
elif imc >= 25:
    print('Peso em excesso')
elif imc >= 18.5:
    print('Saudável')
else:
    print('Abaixo do peso')# Operadores lógicos: utilizar not (negação), and (E) e or (OU)
# Dada a idade de uma pessoa, exiba se essa pessoa está apta a votar

idade = int(input('Escreva sua idade: '))
if idade >= 16:
    print('Apto a votar')
# pode escrever else:
print('Não está apto a votar')

# Soma entre dois números
op = input('Deseja somar? (S/N)')
if op == "S":
    x = int(input("Digite um número: "))
    y = int(input("Digite um número: "))
    resultado = x + y
    print("O resultado da some é" , resultado)
else: 
    print("Ate a próxima")

# Soma ou multiplicação de dois números
pergunta = input('Deseja somar (S) ou multiplicar (M)?')
if pergunta != 'S' and pergunta != 'M':
    print('Opção inválida')
else:
    z = int(input("Digite um número: "))
    w = int(input("Digite um número: "))
    if pergunta == 'S':
        soma = z + w
        print('O resultado da soma é', soma)
    else:
        multiplicacao = z * w
        print('O resultado da multiplicação é', multiplicacao)

# Verificar se aluno está aprovado
nota = float(input('Isira a nota do aluno: '))
if nota >= 7:
    print('Aprovado')
elif nota >= 1.7:
    print('Em recuperação')
else:
    print('Reprovado')

# Verificar se números são iguais
a = int(input('Insira um número: '))
b = int(input('Insira um número: '))
c = int(input('Insira um número: '))
if a == b == c:
    print('Iguais.')
else:
    print('Não iguais')

# Verificar se aluno está aprovado a partir de 3 notas
prova1 = float(input('Insira a nota da primeira prova do(a) aluno(a): '))
prova2 = float(input('Insira a nota da segunda prova do(a) aluno(a): '))
prova3 = float(input('Insira a nota da terceira prova do(a) aluno(a): '))
mediaAluno = (prova1+prova2+prova3)/3
if mediaAluno >= 6 and prova1 >= 5 and prova2 >= 5 and prova3 >= 5:
    print('Aprovado')
else:
    print('Reprovado')

# Ler ano e verificar se el é bissexto, par ou ímpar
ano = int(input('Insira um ano: '))
if ano%4 == 0:
    print('Ano', ano, 'é bissexto e par.')
elif ano%4 != 0 and ano%2 == 0:
    print('Ano', ano, 'é par, mas não bissecxto.')
else:
    print('Ano', ano, 'é ímpar.')

# Leia dois números quaisquer e dividir o primeiro pelo segundo (evitando divisão por zero). Caso o segundo valor seja zero, informe como resposta "Erro: divisão por zero!".
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
if n2 == 0:
    print('Erro: divisão por zero!')
else:
    print(n1/n2)

# Ler dois números inteiros e exibir o maior deles. Escreve o valor mesmo que o usuário tenha informado números iguais.
n3 = int(input('Insira um número: '))
n4 = int(input('Insira outro número: '))
if n3 > n4:
    print('O número', n3, 'é o maior.')
elif n4 > n3:
    print('O número ', n4, ' é o maior.')
else:
    print('Os dois números são iguais.')

# Ler um número inteiro e imprimir se ele é par ou ímpar. Use como saída as strings "Par" e "Ímpar".
n5 = int(input('Insira um número: '))
if n5%2==0:
    print('O número é par.')
else:
    print('O número é ímpar.')

# Ler três números inteiros e exibir o maior deles. Exiba apenas o valor do maior.
n6 = int(input('Insira um número: '))
n7 = int(input('Insira outro número: '))
n8 = int(input('Insira outro número: '))
if n6 > n7 and n6 > n8:
    print('O maior número entre os 3 é o', n6)
elif n7 > n6 and n7 > n8:
    print('O maior número entre os 3 é o', n7)
else:
    print('O maior número entre os 3 é o',n8)

# Faça um programa que calcule o IMC de uma pessoa e informe a sua classificação
peso = float(input('Insira o peso em kg (ex: 72): '))
altura = float(input('Insira a altura em metros (ex: 1.73): '))
imc = peso/(altura*altura)
if imc >= 40:
    print('Obesidade Grau III')
elif imc >= 35:
    print('Obesidade Grau II')
elif imc >= 30:
    print('Obesidade Grau I')
elif imc >= 25:
    print('Peso em excesso')
elif imc >= 18.5:
    print('Saudável')
else:
    print('Abaixo do peso')