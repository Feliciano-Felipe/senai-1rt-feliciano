numero = int(input("Insira um número: "))

for cont in range(1,11):
    resultado = numero * cont
    print("{} * {} = {}".format(numero,cont,resultado))