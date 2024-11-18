# Meu Mercado

# Funções
def cadastrar(produtos):
    codigo = int(input('\nCódigo do produto: '))
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    estoque = int(input('Quantidade em estoque: '))

    produtos[codigo] = [nome, preco, estoque]

def listar(produtos):
    for produto in produtos:
        nome, preco, estoque = produtos[produto]
        print(f'Produto [{produto}]: {nome:7} - preço: R${preco:6.2f} - {estoque:5d} em estoque.')

def buscar_codigo(produtos):
    produto = int(input('Código: '))
    if produto in produtos:
        nome, preco, estoque = produtos[produto]
        print(f'\nProduto [{produto}]: {nome} - preço: R${preco:.2f} - {estoque} em estoque.')
    else:
        print('\nProduto não encontrado.')

def buscar_nome(produtos):
    nome_desejado = input('Nome do produto: ')
    for produto in produtos:
        nome, preco, estoque = produtos[produto]
        if nome == nome_desejado:
            print(f'\nProduto [{nome_desejado}]: preço: R${preco:.2f} - {estoque} em estoque.')
            return
    
    print('\nProduto não encontrado.')

def remover(produtos):
    produto = int(input('Código: '))
    if produto in produtos:
        del produtos[produto]
        print('\nProduto removido.')
    else:
        print('\nProduto não encontrado.')

def comprar(produtos):
    produto = int(input('Código: '))
    if produto in produtos:
        quantidade = int(input('Quantidade comprada: '))
        nome, preco, estoque = produtos[produto]
        if quantidade <= estoque:
            custo = preco * quantidade
            print(f'\nProduto [{produto}]: {nome} comprada pelo valor de R${custo:.2f}.')
            produtos[produto][2] -= quantidade
            return custo
        else:
            print(f'Quantidade solicitada não disponível. Temos {estoque} em estoque.')
    else:
        print('\nProduto não encontrado.')

def comprar_lista(produtos):
    listar(produtos)
    total = 0.0

    produto = int(input('Código (-1 para fechar sacola): '))
    while produto != -1:
        if produto in produtos:
            quantidade = int(input('Quantidade comprada: '))
            nome, preco, estoque = produtos[produto]
            if quantidade <= estoque:
                custo = preco * quantidade
                print(f'\nProduto [{produto}]: {nome} comprada pelo valor de R${custo:.2f}.')
                produtos[produto][2] -= quantidade
                total += custo
            else:
                print(f'Quantidade solicitada não disponível. Temos {estoque} em estoque.')
        else:
            print('\nProduto não encontrado.')
        produto = int(input('Código (-1 para fechar sacola): '))
    print(f'Total da compra é de R${total:.2f}')

# código, nome, preço e estoque
# Diciionário
produtos = {
    1: ['alface', 0.31, 200],
    2: ['tomate', 2.10, 1000],
    3: ['maçã', 9.87, 2000],
    4: ['batata', 1.05, 500]
}

# Menu com opções
def menu():
    print('''\nEscolha uma opção:\n
          1. Cadastrar produto
          2. Listar produtos
          3. Buscar produto pelo código
          4. Buscar produto pelo nome
          5. Remover produto
          6. Comprar produto
          7. Comprar lista de produtos
          8. Sair
          ''')

while True:
    menu()
    opcao = int(input('Escolha uma opção: \n'))
    if opcao == 1:
        cadastrar(produtos)
    elif opcao == 2:
        listar(produtos)
    elif opcao == 3:
        buscar_codigo(produtos)
    elif opcao == 4:
        buscar_nome(produtos)
    elif opcao == 5:
        remover(produtos)
    elif opcao == 6:
        comprar(produtos)
    elif opcao == 7:
        comprar_lista(produtos)
    elif opcao == 8:
        print('Sair')
        break
    else:
        print('Opcção inválida.')
