# Múltipla escolha
# Case é utilizado em versões 3.1 ou acima do python
print('Escolha entre [T]riângulo, [Q]uadrado, [R]etângulo ou [C]írculo: ')
op = input()

match op:
    case 'T':
        print('Você escolheu triângulo.')
    case 'Q':
        print('Você escolheu quadrado.')
    case 'R':
        print('Você escolheu retângulo')
    case 'C':
        print('Você escolheu círculo.')
    case default:
        print('Opção inválida.')

# Forçar intervalo de valores
# ex1
op = '0'
while op != 'F' and op != 'M':
    op = input('Sexo [F]eminino ou [M]asculino?')

# ex2
graus = -1
while graus < 0 or graus > 360:
    graus = int(input('Graus entre 0 e 360: '))

# ex3
numero = 1
while numero <= 100:
    print(numero)
    numero = numero + 1

# ex4
numero = 1
cont = 0
for numero in range(1, 101):
    if numero % 11 == 0:
        cont = cont + 1
print('São', cont, 'mútiplos de 11.')

# Usando valor de incremento, somatorial
# ex1
a = int(input('Valor inicial: '))
b = int(input('Valor final: '))
soma = 0
for i in range(a, b+1):
    soma = soma + i
print('Soma de', a, 'até', b, 'é', soma)

# ex2
n = int(input('Valor final: '))
soma = 0
for i in range(1, n+1):
    soma = soma + i
print('Soma de 1 até', n, 'é', soma)

# ex3 Fatorial de n:n!=n*(n-1)!
n = int(input('Valor final: '))
fatorial = 1
for i in range(1, n+1):
    fatorial = fatorial * i
print(n, '! = ', fatorial)

# Flag/bandeira indica se uma condição aconteceu
# ex1 Existe um número múltiplod e 17 entre 100 e 200?
flag = False  # por enquanto é falso
for i in range(100, 200):
    if i % 17 == 00:
        flag = True
        break
if flag:
    print('Encontramos múltiplo de 17 entre 100 e 200.')
else:
    print('Não foi encontrado.')
