# # 1. Escreva um programa em Python que solicite ao usuário o ano atual e o ano em que ele nasceu. Com base nesta informação (independente do dia de hoje) calcule a idade dele e informe se:

# # O usuário não pode votar (menor do que 16 anos);
# # Tem voto facultativo (entre 16 e 18 ou maior do que 65);
# # É obrigado a votar (entre 18 e 65 anos).

ano = int(input("Informe o ano atual: "))
nasc = int(input("Informe o ano de nascimento: "))

idade = ano - nasc

if idade < 16:
    print("Não pode votar")
elif idade <= 18 or idade > 65:
    print("Voto facultativo")
else:
    print("Voto obrigatório")


# # 2. Escreva um programa em Python que solicite 3 números ao usuário e retorne qual destes é o maior número.
num1 = int(input("Informe um número: "))
num2 = int(input("Informe um segundo número: "))
num3 = int(input("Informe um terceiro número: "))

maior = max(num1, num2, num3)

print(f"O maior número é {maior}.")

# # 3. Escreva um programa em Python que solicite um número ao usuário e retorne a tabuada do número informado.

num = int(input("Informe um número: "))
i = 1
while i <= 10:
    print (num, "x", i, "=", num*i)
    i = i + 1

# 4. Escreva um programa em Python que solicite 2 números inteiros ao usuário e percorra estes números informando:

# “Fizz”, caso o número seja divisível por 3;
# “Buzz”, caso o número seja divisível por 5;
# “FizzBuzz” caso o número seja divisível por 3 e por 5;
# O próprio número, caso o número não seja divisível nem por 3 nem por 5.

x = int(input("Informe um número: "))
if x % 3 == 0 and x % 5 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 ==0:
    print("Buzz")
else:
    print(x)