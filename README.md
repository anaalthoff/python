# Algoritmos e Programação em Python

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-brightgreen)
![Licença](https://img.shields.io/badge/licença-MIT-blue)

Esse repositório reúne os exercícios, anotações e projetos desenvolvidos ao longo dos meus estudos em **Análise e Desenvolvimento de Sistemas**, partindo dos fundamentos da linguagem e avançando gradualmente até estruturas de dados, funções, recursividade, programação orientada a objetos e análise estatística de dados.

## Sumário

- [Sobre o projeto](#sobre-o-projeto)
- [Objetivos de aprendizagem](#objetivos-de-aprendizagem)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Pré-requisitos](#pré-requisitos)
- [Como executar](#como-executar)
- [Tecnologias e bibliotecas](#tecnologias-e-bibliotecas)
- [Licença](#licença)

## Sobre o projeto

Cada arquivo concentra um conjunto de exercícios sobre um tema específico da programação, com comentários explicativos que documentam a lógica aplicada e, em vários casos, apresentam **soluções alternativas** para o mesmo problema (por exemplo, resolvendo um mesmo exercício com `while` e com `for`, ou de forma iterativa e recursiva).

O material foi construído de forma incremental e serve tanto como registro do aprendizado quanto como material de consulta rápida.

## Objetivos de aprendizagem

- Consolidar a **lógica de programação** e a construção de algoritmos.
- Dominar **estruturas condicionais** e **estruturas de repetição**.
- Manipular **listas, vetores, matrizes, tuplas, dicionários e conjuntos**.
- Trabalhar com **strings** e formatação de saída.
- Escrever **funções**, incluindo funções de alta ordem e **recursividade**.
- Aplicar os conceitos de **Programação Orientada a Objetos (POO)**.
- Introduzir **estatística e probabilidade** com apoio de bibliotecas científicas.

## Estrutura do repositório

| Tema | Conteúdo abordado |
|---|---|
| Fundamentos | Entrada/saída, variáveis, tipos, saída formatada, cálculos geométricos, frações, MMC e potenciação |
| Estruturas condicionais | `if`/`elif`/`else`, operadores lógicos, cálculo de IMC, ano bissexto, maior de N números |
| Estruturas de repetição | `while` e `for`, fatorial, tabuada, série de Fibonacci, contadores e médias |
| Controle de fluxo | `break`, números aleatórios (`random`), valor absoluto e avaliação de expressões (`eval`) |
| Seleção múltipla | `match`/`case`, validação de intervalos, uso de *flags* e somatórios |
| Listas e vetores | Iteração, `append`, inversão, produto escalar, busca, interseção e ordenação |
| Strings | Manipulação e fatiamento, cifra de deslocamento (ASCII), `split`, ordenação alfabética |
| Matrizes | Listas bidimensionais, *list comprehensions*, matriz identidade, busca de mínimos/máximos |
| Coleções | Tuplas, dicionários e conjuntos (*sets*) e conversões entre tipos |
| Funções | Definição, parâmetros, retorno e menu de cálculo de áreas |
| Recursividade | Fatorial, somatório, Fibonacci, MDC, exponenciação e funções como parâmetro |
| Exercícios aplicados | Faixa etária de voto, maior de três, tabuada e *FizzBuzz* |
| Exercícios aplicados | Cálculo de desconto/acréscimo e análise de salários |
| Listas | Fundamentos de criação, preenchimento e iteração de listas |
| Revisão | Variáveis, operações matemáticas, decisões, repetições e listas |
| Compilado | Coletânea de exercícios variados de revisão |
| Projeto | Sistema de gestão de estoque com CRUD baseado em dicionários e menu interativo |
| POO | Classes `Animal`, `Livro`, `Funcionario`, `Produto` e `ContaCorrente` (herança e encapsulamento) |
| POO | Classe `Aluno` com métodos de cálculo de idade e gestão de disciplinas |
| Probabilidade | Cálculo do escore Z e distribuição normal com `scipy` |
| Estatística | Média, mediana, variância, desvio padrão e regressão linear com `pandas` e `matplotlib` |

## Pré-requisitos

- [Python 3.10 ou superior](https://www.python.org/downloads/) — a instrução `match`/`case` presente em alguns exercícios requer Python 3.10+.
- Para os arquivos de **estatística e probabilidade**, instale as bibliotecas científicas:

```bash
pip install numpy pandas scipy scikit-learn matplotlib
```

## Como executar

```bash
# Clone o repositório
git clone https://github.com/anaalthoff/python.git

# Acesse a pasta do projeto
cd python

# Execute o exercício desejado
python 01_fundamentos.py
```

> **Observação:** grande parte dos exercícios utiliza a função `input()` e, portanto, é interativa — os valores são solicitados durante a execução no terminal.

## Tecnologias e bibliotecas

- **Python** — linguagem principal.
- **NumPy** — operações matemáticas e vetoriais.
- **pandas** — manipulação e análise de dados.
- **SciPy** — cálculos estatísticos avançados.
- **scikit-learn** — modelagem e análise preditiva.
- **Matplotlib** — visualização de dados.

## Licença

Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para estudar, utilizar e adaptar o conteúdo.
