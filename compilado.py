#Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
a = int(input('Insira um número: '))
b = int(input('Insira um número: '))
c = int(input('Insira um número: '))

# a função abs() é usada para calcular o valor absoluto
maior_ab = int((a + b + abs(a - b)) / 2)
maior = int((maior_ab + c + abs(maior_ab - c)) / 2)

print(f"{maior} eh o maior")

# Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.
def calcular(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular(n - 1)
    
def calcular(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial

while True:
    n = int(input("Insira um número entre 1 e 12: "))

    if 1 <= n <= 12:
        resultado = calcular(n)
        print(resultado)
        break

#Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Na saída escreva o quadrante a que ele pertence.
while True:
    try:
        x = int(input('Insira a coordenada X: '))
        y = int(input('Insira a coordenada Y: '))

        if isinstance(x, int) and isinstance(y, int):
            if x > 0 and y > 0:
                print("primeiro")
            elif x < 0 and y > 0:
                print("segundo")
            elif x < 0 and y < 0:
                print("terceiro")
            elif x > 0 and y < 0:
                print("quarto")
            else:
                print("Origem")
            break
    except ValueError:
        pass  # Não exibe mensagem de erro, apenas continua o loop

# Dada a quantidade de refeições disponíveis para cada escolha e o número de refeições pedidas para cada escolha, quantos passageiros seguramente não poderão ser atendidos?
disponivel_frango = int(input('Quantidade disponível de frango: '))
disponivel_bife = int(input('Quantidade disponível de bife: '))
disponivel_massa = int(input('Quantidade disponível de massa: '))

req_frango = int(input('Quantidade solicitada de frango: '))
req_bife = int(input('Quantidade solicitada de bife: '))
req_massa = int(input('Quantidade solicitada de massa: '))

# Calculando a diferença entre a quantidade disponível e a quantidade requisitada para cada tipo de refeição
dif_frango = req_frango - disponivel_frango
dif_bife = req_bife - disponivel_bife
dif_massa = req_massa - disponivel_massa

# Calculando o número total de passageiros que não serão atendidos
passageiros_sem_refeicao = max(0, dif_frango) + max(0, dif_bife) + max(0, dif_massa)

# Imprimindo o resultado
print(passageiros_sem_refeicao)

# A função max(a, b) retorna o valor máximo entre a e b. No contexto do código fornecido, max(0, dif_frango) é usado para garantir que o resultado seja no mínimo 0. Aqui está o funcionamento detalhado:

# Se dif_frango for positivo, significa que há mais refeições pedidas do que disponíveis. Nesse caso, max(0, dif_frango) retorna dif_frango, representando a diferença entre as refeições pedidas e disponíveis.

# Se dif_frango for zero ou negativo, significa que há refeições suficientes ou até mais do que suficientes. Nesse caso, max(0, dif_frango) retorna 0, indicando que não há passageiros não atendidos para esse tipo de refeição.

# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
# Perimetro = XX.X
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
# Area = XX.X
# Leitura dos valores de entrada
A = float(input('Insira um número: '))
B = float(input('Insira outro número: '))
C = float(input('Insira outro número novamente: '))

# Verificação se forma um triângulo
if A + B > C and A + C > B and B + C > A:
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    area_trapezio = ((A + B) * C) / 2
    print(f"Area = {area_trapezio:.1f}")