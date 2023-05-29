while True:
    numero = int(input("Digite um número: "))

    if numero < 0:
        print("Negativo não, besta. Parece até o Gregório")
        break

    if numero % 2 == 0:
        print("O número {} é par.".format(numero))
    else:
        print("O número {} é ímpar.".format(numero))
