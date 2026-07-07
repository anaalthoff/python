# Crie as seguintes classes em Python. Crie objetos para verificar o seu funcionamento:

# 1. Crie uma classe Animal:

# A classe deve ter os atributos nome e especie;
# Defina um método som que imprima um som característico do animal;
# Delimite algumas espécies para definir o som.

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def som(self):
        print("Som genérico de animal.")

class Cachorro(Animal):
    def som(self):
        print("Au Au!")

class Gato(Animal):
    def som(self):
        print("Miau!")

# Teste
rex = Cachorro("Laika", "cachorro")
felix = Gato("Lola", "gato")

# 2. Crie uma classe Livro:

# A classe deve conter os atributos titulo, autor e ano;
# Defina um método descricao que retorne uma string formatada com essas informações.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descricao(self):
        return f"'{self.titulo}' escrito por {self.autor} em ({self.ano})"

# Teste
livro1 = Livro("1984", "George Orwell", 1949)
print(livro1.descricao())

# 3. Crie uma classe Funcionario:

# A classe deve ter os atributos nome e salario (privado);
# Defina um método aumento que recebe um percentual e, com base neste valor, altere o valor do atributo o salário.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario  # atributo privado

    def aumento(self, percentual):
        self.__salario *= (1 + percentual / 100)

    def mostrar_salario(self):
        return f"Salário de {self.nome}: R$ {self.__salario:.2f}"

# Teste
func = Funcionario("Ana", 8000)
func.aumento(10)
print(func.mostrar_salario())

# 4. Crie uma classe Produto:

# A classe deve ter os atributos nome e preco;
# Defina um método que calcule o novo preço do produto a partir de um percentual de desconto informado.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        novo_preco = self.preco - desconto
        return f"Preço com desconto: R$ {novo_preco:.2f}"

# Teste
p = Produto("Notebook", 5000)
print(p.aplicar_desconto(10))

# 5. Crie uma classe ContaCorrente

# Deve conter atributos para titular, saldo (privado) e limite (privado);
# Defina métodos para depositar, sacar e exibir o saldo atualizado.

class ContaCorrente:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado.")

    def sacar(self, valor):
        if valor <= self.__saldo + self.__limite:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        return f"Saldo de {self.titular}: R$ {self.__saldo:.2f}"

# Teste
conta = ContaCorrente("João", 1000, 500)
conta.depositar(200)
conta.sacar(1100)
print(conta.exibir_saldo())