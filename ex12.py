# 1. Escreva um programa em Python que solicite ao usuário o ano atual e o ano em que ele nasceu. Com base nesta informação (independente do dia de hoje) calcule a idade dele e informe se:

# O usuário não pode votar (menor do que 16 anos);
# Tem voto facultativo (entre 16 e 18 ou maior do que 65);
# É obrigado a votar (entre 18 e 65 anos).

ano = int(input("Informe o ano atual: "))
nasc = int(input("Informe o ano de nascimento: "))

idade = ano - nasc

if idade < 16:
    print("Não pode votar")
elif idade <= 18 or idade > 65:
    print("Voto facultativo")
else:
    print("Voto obrigatório")


# 2. Escreva um programa em Python que solicite 3 números ao usuário e retorne qual destes é o maior número.




# 3. Escreva um programa em Python que solicite um número ao usuário e retorne a tabuada do número informado.



# 4. Escreva um programa em Python que solicite 2 números inteiros ao usuário e percorra estes números informando:

# “Fizz”, caso o número seja divisível por 3;
# “Buzz”, caso o número seja divisível por 5;
# “FizzBuzz” caso o número seja divisível por 3 e por 5;
# O próprio número, caso o número não seja divisível nem por 3 nem por 5.