# abs() -> traz o valor absoluto, ou o módulo de um número, que é a distância desse número até o zero.
# eval() -> converter string para float ou int automaticamente

# Encontre o primeiro múltiplo de 37 acima de 200
n = 200
while(True):
    n = n + 1
    if n%37 == 0:
        print('Encontrei: ',n)
        break #sai do laço

#Jogo do Pim - encontrar múltiplos de 4 até 30
n = 0
while(n<30):
    n = n + 1
    if n%4 == 0:
        print('Múltiplos de 4: ',n)

# Sorteio número aleatório entre 1 e 5
import random
numero = random.randint(1,5)
chute=int(input('Insira um número de 1 a 5: '))
if chute == numero:
    print('Acertou!')
else:
    print('Não foi dessa vez.')

# Sorteio número aleatório entre 1 e 5, mas agora o usuário tem várias tentativas
import random
numero = random.randint(1,5)
chute = numero + 1
while chute != numero:
    chute=int(input('Insira um número de 1 a 5: '))
    if chute != numero:
        print('Errou, tente novamente.')
print('Acertou!')

# Ler um número inteiro e imprimir o módulo do número lido
num = int(input('Insira um número: '))
modulo = abs(num)
print(f'O módulo do número é: {modulo}')

# Leia uma expressão aritmética definida pelo usuário e exiba a resposta da expressão
expressao = input('Digite uma expressão aritmética: ')

try:
    resultado = eval(expressao)
    print(f'O resultado da expressão é: {resultado}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')