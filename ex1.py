# Para rodar, escrever 'python + nome do arquivo.py'
print("Hello, world!")

# Este programa calcula a área do triângulo retângulo
altura = 15
base = 3
area = (altura*base)/2
print(area)

# Caracteres especiais: \n - nova linha, \r - volta para início da linha, \t - tabulação, \\contra barra

# Imprimir o tipo da variável
print(type(area))

# Entrada de dados
altura2 = float(input('Digite a altura do triângulo: '))
base2 = float(input('Digite a base do triângulo: '))
# Quando utiliza a função input, os dados são armazenados como strings, por isso necessário converter
area2 = (altura2*base2)/2
print('A área do triângulo é: ', area2)

# Saída formatada de dados
# %f - usado para números do tipo float
# %d - para números inteiros
# %s - para strings
i = 0
pi = 3.1415
print('inteiro: %d\n' %i)
print('pi: %.2f\n' %pi)

# Ler 2 números, calcular a soma, mostrar os números lidos e resultado da soma
x = float(input('Insira um número: '))
y = float(input('Insira outro número: '))
soma = x + y
print('X é igual a',x,'Y é igual a',y,'e o resultado da soma deles é %.2f\n' %soma)

# Ler 2 números inteiros. Multiplicar o 1º por 4 e o 2º por 0,6. Calcular a média aritmética dos resultados obtidos. Imprimir os valores lidos, os calculados e a média aritmética.
a = int(input('Insira um número: '))
b = int(input('Insira outro número: '))
aMultiplicado = a*4
bMultiplicado = b*0.6
media = (aMultiplicado + bMultiplicado)/2
print('A é igual a',a,'B é igual a',b,'após multiplicados ficam',aMultiplicado,'e',bMultiplicado,'e a média aritmética deles é',media,'.\n')

# Ler 2 números e inverter seus valores.
c = int(input('Insira um número: '))
d = int(input('Insira outro número: '))
novoC = d
novoD = c
print('O primeiro número agora é ',novoC, 'e o segundo número agora é ',novoD, '.\n')

# Ler uma temperatura em graus Celsius e apresentá-la em Fahrenheit.
C = float(input('Insira a temperatura em graus Celsius: '))
F = (9*C+160)/5
print(C,'graus Celsius equivale a %.1f' %F,'graus Fahrenheit. \n')

# Ler o nome do aluno, suas 3 notas e informar sua média aritmética.
nome = (input('Insira o nome do(a) aluno(a): '))
prova1 = float(input('Insira a nota da primeira prova do(a) aluno(a): '))
prova2 = float(input('Insira a nota da segunda prova do(a) aluno(a): '))
prova3 = float(input('Insira a nota da terceira prova do(a) aluno(a): '))
mediaAluno = (prova1+prova2+prova3)/3
print('O(a) aluno(a)',nome,'obteve a média %.2f' %mediaAluno,'ao final do semestre. \n')

# Calcular a área de uma elipse.
r1 = float(input('Insira o raio maior da elipse: '))
r2 = float(input('Insira o raio menor da elipse: '))
pi = 3.14
n = pi*r1*r2
print("Área da elipse é: ", n)

# Calcular o MMC entre dois números.
# def é uma palavra-chave usada para definir uma função
def mmc(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          result = z
          break
      z += 1
  return result

x=5
y=10
result=mmc(x, y)

print("Minimo Múltiplo Comum de: ")
print("x=%d" % x)
print("y=%d" % y)
print("Resultado= %d" % result)