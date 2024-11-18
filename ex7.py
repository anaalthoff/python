# Strings
# Pode concatenar strings com +, multiplar com *, acessar os elementos com [] e verificar tamanho com len
# Sao imutaveis. Para alterar um elemento se faz o seguinte: str1 = str1.replace('M', 'n')
# Para verificar se existem substrings: if 'Ola' in str1
# Para verificar se nao existe uma substring: if 'Ola' not in str1
# Para verificar onde está a substring: pos1 = str1.find('Mundo')
# Parar separar a string: lista = str1.split(<separador>, <maxsplit>)

# Funções para usar com listas:
# len(<lista>) comprimento
# min(<lista>) menor item
# max(<lista>) maior item
# sum(<lista>) soma
# lista.append(<item>) inclui item ao final
# lista.count(<item>) conta
# lista.insert(n, <item>) insere item na posicao n
# lista.pop() remove o último elemento
# lista.remove(<item>) remove a primeira ocorrência do item na lista
# lista.reverse() inverte a ordem
# lista.slice[:inicio :fim :passo]
# lista.sort() ordena em ordem alfabética

# Método format: print('Meu {0} disse '"{0}!"'.format('amigo','ola' )). Pode deixar com ou sem número, o número dá a ordem
# Método format: print('Este {objeto} é {adjetivo}.'.format(objeto='oculos', adjetivo='muito feio'). São chamados de apelidos
# ano = 2023, disciplina = 'Algoritmos', f'Em {ano} eu aprendi {disciplina}.'
# ano = 2023, chance = 0.4967, 'Ano {:-9} tem {:2.2%} de chance.'.format(ano, chance). Haverá 9 casas e serão 2 casas decimais antes e 2 depois, e % é porcentagem
# ano = 2023, disciplina = 'Algoritmos', f'Em {ano:b} eu aprendi {disciplina}.' Irá mudar o formato do ano para binário

# Criar a criptografia de uma senha. Na primeira passada, somente caracteres que sejam minúscula se maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII. ex: a vira d. Na segunda passada, linha deve ser invertida. Na terceira, todo e qualquer caracter a partir da metade em diante deve ser deslocado uma posiçaço para esquerda na tabela ASCII. Ex: b vira a.
frase = input("Escreva alguns caracteres: ")

passo1 = ''

for i in frase:
    if i.isalpha():
        # Se i for uma letra (i.isalpha()), ela é convertida para um código ASCII (ord(i)), somada a 3, e convertida de volta para um caractere chr()
        passo1 = passo1 + chr(ord(i)+3)
    else:
        passo1 = passo1 + i
print("Passo1: ", passo1)

# Inverter
passo2 = passo1[::-1]
print("Passo2: ", passo2)

meio = int(len(passo2)/2)
# a notação de slice ([:]) é utilizada para extrair uma parte de uma sequência (como uma string)
passo3 = passo2[:meio]
for i in range(meio, len(passo2)):
    passo3 = passo3 + chr(ord(passo2[i])-1)
print("Passo3: ", passo3)

# Escreva um algoritmo que permita a leitura de 7 nomes e coloque em uma lista. Exiba a lista de trás para frente, exibindo no início o último nome informado e o ao final da lista o primeiro. Exiba um nome a cada linha.
nomes = []

for i in range(7):
    nome = input("Escreva um nome")
    nomes.append(nome)

# nomes.reverse()

# for nome in reversed(nomes):
for nome in nomes[::-1]:
    print(nome)

# Ler uma frase, separar palavra por palavra e exibir cada palavra em uma linha.
frase = input("Digite uma frase: ")

palavras = frase.split()

for palavra in palavras:
    print(palavra)

# Ler o nome de 20 pessoas e exibir ao final a lista de nomes em ordem alfabética. Exibir um nome por linha.
nomes = []

for i in range(20):
    nome = input("Digite um nome: ")
    nomes.append(nome)

nomes.sort()

for nome in nomes:
    print(nome)

# Ler 10 strings contendo números ou expressões aritméticas. Após ler as strings, avaliar as expressões e somar o resultado de todas as 10. Exiba o valor da soma ao final como ponto flutuante (float).
soma = 0.0

for i in range(10):
    expressao = input("Digite uma expressão aritmética: ")

    result = eval(expressao)
    soma += result

print(f"A soma das expressões é: {soma}")

# Inverter a primeira metade de uma string. Salvar a string com a nova configuração.
frase = input("Escreva alguns caracteres: ")

passo1 = ''

meio = int(len(frase)/2)
parte1 = frase[:meio]
invertida = parte1[::-1]
nova = invertida + frase[meio:]

print("Nova frase:", nova)