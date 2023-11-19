#Calcular a média
n = int(input)

media = 0
for i in range (n):
    media = media + float(input())
media = media/n

print(media)

# Iterar números
notas=[8,8.8,9]
for i in range(3):
    print(notas[i])

# Outra forma
for i in notas:
    print(i)

#Iterar números informando quantos elementos terá a lista
notas=[0,0,0]
notas[0] = float(input('Primeira nota: '))
notas[1] = float(input('Segunda nota: '))
notas[2] = float(input('Terceira nota: '))

for i in range(3):
    print(notas[i])

#Iterar números com uma lista vazia inicialmente
notas=[]
notas.append(float(input('Primeira nota: ')))
notas.append(float(input('Segunda nota: ')))
notas.append(float(input('Terceira nota: ')))

#Retorna o tamanho da lista
tam=len(notas)
for i in range(tam):
    print(notas[i])

# Outra forma
for i in range(len(notas)):
    print(notas[i])

#Criar uma lista com tamanho n informado pelo usuário
n = int(input('Insira o tamanho da lista: '))
lista = [0] * n
for i in range(n):
    lista[i] = i+1
print(lista)