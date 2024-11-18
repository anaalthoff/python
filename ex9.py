# Tuplas, dicionários e conjuntos

# Tuplas são listas imutáveis, assim como strings. Podem ser de diferentes tipos. Nas listas é possível alterar, remover e adicionar elementos.
# tuplas = (2,3); listas = [2,3]

# Dicionários são coleções de itens e seus elementos. Sua sintaxe básica é: {'chave': 'valor'}. Utiliza-se {} para delimitar o dicionário e a chave é separada do valor por dois pontos :. Este valor aceita diversos tipos: listas, outros dicionários, inteiros, strings e etc.

# Listas e tuplas são indexadas por inteiros, ao passo que dicionários podem ser indexados por strings.

# Conjuntos são estruturas utilizadas para representar coleções desordenadas de elementos únicos. Não contém elementos repetidos. Não confiar na ordem dos elementos. Pode conter apenas ovjetos imutáveis como inteiros, tuplas, etc, não pode modificar seus elementos internos, mas pode adicioanr novos.
# < - conj da esquerda está contido no da direita
# > - conj da direita está contido no da esquerda
# | ou método union - união
# & ou método intersection - intersecção

# Lista:
contato = ['Tiago', '9999-9999']
type(contato)

# Tupla:
contato = ('Mauricio', '8888-8888')
type(contato)

# Dicionário:
contato = {'Andre': '7777-7777'}
type(contato)
print(contato['Andre'])

# Conjunto ou set:
contato = {'Ramon', '6666-666'}
type(contato)

# É possível transformar um tipo em outro. Exemplo de tupla para dicionário, de lista para conjutno/set
agenda = (('Tiago', '9999-9999'),('Mauricio', '8888-8888'))

contatos = dict(agenda)
print(contatos)

minha_lista = [1,2,3,4,5]
meu_conjunto = set(minha_lista)
print(meu_conjunto)

print(contatos['Mauricio'])
print(contatos.get('André', 'Contato não encontrado'))
print('9999-9999' in contatos.values())

# Para adicionar um valor no dicionário
contatos['André'] = '5555-5555'
print(contatos)

# Para remover um valor
del contatos['André']
print(contatos)
# OU
print(contatos.pop('André', 'Contato não encontrado'))

# Para alterar
contatos['Mauricio'] = '9849-9849'
print(contatos)

# Adicionando um elemento a todos os elementos do dicionário
for i in contatos:
    contatos[i] = '9' + contatos[i]
print(contatos)
# OU
contatos = {nome : '9' + contatos[nome] for nome in contatos}
print(contatos)