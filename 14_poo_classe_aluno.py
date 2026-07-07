# Crie uma classe em Python chamada Aluno, conforme segue:

# A classe Aluno deve ter os atributos nome, dataNascimento, telefone, curso, disciplinas (dicionário com as disciplinas em que o aluno está/esteve matriculado - O dicionário deverá conter o nome da disciplina (chave) e a situação (valor));
# Defina um método que retorne a idade do aluno;
# Defina um método que adicione uma disciplina para o aluno, a situação padrão de entrada deve ser "Matriculado";
# Defina um método que altere a situação do aluno quanto a disciplina. As situações possíveis são: Matriculado, Cancelado, Aprovado e Reprovado.
# Defina um método que retorne todas as informações a respeito do aluno.
# Envie a definição da classe e seus métodos, além de exemplos da instanciação do objeto e uso de seus métodos.

from datetime import datetime

class Aluno:
    def __init__(self, nome, dataNascimento, telefone, curso):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.curso = curso
        self.disciplinas = {}

    def idade(self):
        ano = datetime.today()
        idade = ano.year - self.dataNascimento
        return idade

    def adicionar_disciplina(self, nome_disciplina):
        self.disciplinas[nome_disciplina] = "Matriculado"

    def alterar_situacao_disciplina(self, nome_disciplina, nova_situacao):
        situacoes = ["Matriculado", "Cancelado", "Aprovado", "Reprovado"]
        if nome_disciplina in self.disciplinas and nova_situacao in situacoes:
            self.disciplinas[nome_disciplina] = nova_situacao

    def listar_disciplinas(self):
        lista = []
        for disciplina, situacao in self.disciplinas.items():
            lista.append(f"{disciplina} ({situacao})")
        return ", ".join(lista)

    def descricao(self):
        return (
            f"{self.nome} nasceu em {self.dataNascimento}, cursa {self.curso} e seu telefone é {self.telefone}. Disciplinas cursadas: {self.listar_disciplinas()}"
        )

# Teste
aluno = Aluno("Ana", 2000, "99999-9999", "Análise e Desenvolvimento de Sistemas")

aluno.adicionar_disciplina("Matemática")
aluno.adicionar_disciplina("Português")
aluno.alterar_situacao_disciplina("Matemática", "Aprovado")
print("\nDescrição do aluno:")
print(aluno.descricao())