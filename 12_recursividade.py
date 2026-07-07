# Recursividade
# Recursividade indireta ou composta: uma função ativa a outra que termina por chamar novamente a primeira

# Fatorial é um bom exemplo:
def fatorial(n):
    # critério de parada:
    if n == 1:
        return 1
    return n * fatorial(n-1)

print(fatorial(5))

# Pedir um número inteiro ao usuário e retornar a soma de todos os números de 1 até o valor informado pelo usuário, ou seja, 1-2-3...n
def somatorio(n):
    # critério de parada
    if n == 1:
        return 1
    # s(n) = (s-1) + s
    return somatorio(n-1) + n

print(somatorio(4))

# Fazer uma função que calcule o n-esimo termo da sequência de Fibonacci
# f(1) = 1
# f(2) = 1
# f(n) = f(n-1) + f(n-2)
def fibanacci(n):
    n_2 = n_1 = fib = 1
    while n > 1:
        #  Calcula-se o próximo termo da sequência de Fibonacci somando os dois termos anteriores
        fib = n_1 + n_2
        n = n-1
        # Atualiza-se n_2 com o valor de n_1, que era o termo anterior
        n_2 = n_1
        # Atualiza-se n_1 com o valor de fib, que agora é o termo mais recentemente calculado
        n_1 = fib
    return fib

# Refazer a anterior usando recursividade
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Calcular o MDC entre dois números
# o MDC de dois números é o mesmo que o MDC do menor deles e do resto da divisão do maior pelo menor.
def mdc(a, b):
    if a < b:
        return mdc(b, a)
    # quando um dos números é zero, o outro é o MDC
    elif b == 0:
        return a
    else:
        return mdc(b, a % b)
# Se a % b for zero, então b é um divisor exato de a, e, portanto, b é o MDC.
# Se a % b não for zero, isso significa que há um resto, e podemos trocar a por b e b por a % b. O MDC entre a e b é o mesmo que o MDC entre b e a % b

# Calcular a exponenciação utilizando apenas operadores aritméticos de soma, subtração, multiplicação e divisão.
def pow(a, b):
    if b == 1:
        return a
    return a * pow(a, b-1)

# Exemplo de recursividade indireta ou composta:
def par(n):
    # o número original era par (pois zero é par)
    if n == 0:
        return True
    return impar(n-1)

def impar(n):
    if n == 0:
        return False
    return par(n-1)

# Função como parâmetro:
def soma(a,b):
    return a + b

def mult(a,b):
    return a * b

def somfat(n, func):
    res = 1
    for i in range(1, n + 1):
        res = func(res, i)
    return res

print('5! = ', somfat(5, mult))
print('soma de 1 a 5 = ', somfat(5, soma))

# Ordenar uma lista a partir de um determinado critério.Ex: crescente, decrescente...
# O critério de ordenação será passado como parâmetro para a função ordena()
def maior(a, b):
    return a > b

def menor(a, b):
    return a < b

def igual(a, b):
    return a == b

def ordena(lista, function):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(tamanho - 1):
            if lista[j]>lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux


# Cifra de César
# Júlio César usava um sistema de criptografia, agora conhecido como Cifra de César, que trocava cada letra pelo equivalente em duas posições adiante no alfabeto (por exemplo, 'A' vira 'C', 'R' vira 'T', etc.). Ao final do alfabeto nós voltamos para o começo, isto é 'Y' vira 'A'. Nós podemos, é claro, tentar trocar as letras com quaisquer número de posições.

# Entrada
# A primeira linha contém uma string com até 50 caracteres maiúsculos ('A'-'Z'), que é a sentença após ela ter sido codificada através desta Cifra de César modificada. A segunda linha contém um número que varia de 0 a 25 e que representa quantas posições cada letra foi deslocada para a direita.
char = input()
n = int(input())

letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
resultado = ''

for j in range(len(char)):
    if char[j].isalpha():
        index = letras.find(char[j].upper())
        index = (index - n) % 26
        resultado += letras[index]
    else:
        resultado += char[j]

print(resultado)

# As Duas Torres 2
# Saruman, o Branco, um grande mago da Terra-média, traiu os bons costumes e se filiou ao lorde do mal, Sauron. Sauron comanda a torre de Minas Morgul, que abriga um dos seus mais temidos servos, o Rei Bruxo de Angmar, um dos Nazgûl (antigos reis humanos que foram corrompidos pelos poderes dos anéis de Sauron). Saruman comanda a torre de Orthanc, onde cria seus servos Uruk-hai, orcs mais terríveis que os convencionais. Para comunicação, eles utilizam as relíquias esféricas chamadas Palantír, que ficam no topo de suas torres.
# A Terra-média avança cada vez mais em tecnologia, muito impulsionada pelas guerras que a acometem diariamente. Um dos problemas que tem atrapalhado sua população é a Interferência de Comunicação Mágica (ICM). Os estudiosos de Minas Tirith, grande cidadela de Gondor, concluíram que para calcular o ICM para Palantír’s, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos. Gandalf, o Cinza, chegou a questionar essa conclusão, alegando que ela não fazia muito sentido, mas ele mesmo concluiu que dar sentido às coisas não faz sentido.
# Saruman e Sauron precisam de uma comunicação estável, pois têm medo que Frodo e seus amigos consigam atrapalhar seus planos, portanto, querem saber quanto de ICM há na comunicação de seus Palantír’s, para que saibam quanto de magia devem empregar na comunicação.

# Você deve fazer uma função chamada calcularICM() para receber a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman. A função deve retornar quanto ICM há na comunicação de seus Palantír’s.

# Entrada
# A função calcularICM() recebe como parâmetro 3 valores inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.
def calcularICM(N, X, Y):
    diametro_sauron = X
    diametro_saruman = Y
    distancia_palantirs = N

    icm = distancia_palantirs / (diametro_sauron + diametro_saruman)

    return icm

# Exemplo
resultado = calcularICM(100,2,2)
print(resultado)

# Número Primo
# Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

def eh_primo(numero):
    # Começa em 2 porque qualquer número é divisível por 1
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        if eh_primo(x):
            print(f'{x} eh primo')
        else:
            print(f'{x} nao eh primo')

main()

# Validador de Senhas
# Rolien e Naej são os desenvolvedores de um grande portal de programação. Para ajudar no novo sistema de cadastro do site, eles requisitaram a sua ajuda. Seu trabalho é fazer um código que valide as senhas que são cadastradas no portal, para isso você deve atentar aos requisitos a seguir:

# A senha deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número;
# A mesma não pode ter nenhum caractere de pontuação, acentuação ou espaço;
# Além disso, a senha pode ter de 6 a 32 caracteres.
# Entrada
# A entrada contém vários casos de teste. A primeira linha tem um inteiro informando a quantidade de casos de teste. Cada linha a seguir tem uma string S, correspondente a senha que é inserida pelo usuário no momento do cadastro.
def validar_senha(senha):
    # Verifica se a senha tem pelo menos 6 e no máximo 32 caracteres
    if 6 <= len(senha) <= 32:
        # Verifica se a senha contém pelo menos uma letra maiúscula, uma letra minúscula e um número
        if any(c.isupper() for c in senha) and any(c.islower() for c in senha) and any(c.isdigit() for c in senha):
            # Verifica se a senha é alfanumerica, não contém caracteres de pontuação, acentuação ou espaço
            if all(c.isalnum() for c in senha):
                return "Senha valida."

    return "Senha invalida."

def main():
    # Número de casos de teste
    n = int(input())

    for i in range(n):
        # Senha inserida pelo usuário
        senha = input().strip()
        # Chama a função validar_senha e imprime o resultado
        print(validar_senha(senha))

main()

# Rico do Mate
# A erva-mate (Ilex paraguariensis) é uma planta nativa da América do Sul que é utilizada para a preparação de uma das bebidas mais característica e apreciada em boa parte da região sul do Brasil, o chimarrão. Normalmente consumido de forma compartilhada, os participantes formam uma roda e vão passando a cuia de mão-em-mão: após ingerir o chá de seu interior, um participante da roda de mate enche a cuia e passa para o próximo.

# Por sua forte presença cultural, existem diversas crenças e lendas associadas à roda de mate, uma delas diz respeito à cuia que leva a última água da garrafa térmica. Segundo a crença, a pessoa mateadora que recebe esta última cuia vai ficar rica, talvez seja uma consolação, pois essa mateadora normalmente recebe menos chá.

# Sabendo desta crença, uma mateadora ávida em programação decidiu fazer uma função para ajudar a descobrir quem será a rica do mate e o quanto de chimarrão ela vai tomar. Para tanto, ela leva em consideração o volume L de água da térmica, a quantidade Q de água que cabe em uma cuia e as pessoas que formam a roda.

# Entrada
# A função deve se chamar rico_do_mate() e receber como parâmetro: o número N (0 < N ≤ 10) de pessoas na roda, seguida por um ponto flutuante L correspondente a quantidade de litros de água que cabem na garrafa térmica (0.0 < L ≤ 20.0), a quantidade Q (0.0 < Q < 1.0) de litros de água que cabem na cuia e uma lista contendo o nome dos participantes, na ordem em que o mate será servido, separados por espaço. Cada nome será fornecido com até 12 caracteres do alfabeto português (26 letras). Os valores de L e Q são fornecidos com exatamente uma casa após o ponto decimal.
def rico_do_mate(N, L, Q, pessoas):
    N_Q = int(L // Q)

    lista = pessoas * 10

    resto = L - (Q * N_Q)
    if resto == 0:
        resto = Q
        N_Q -= 1

    sorteado = lista[N_Q % N]

    print(f"{sorteado} {resto:.1f}")