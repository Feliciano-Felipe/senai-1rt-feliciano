from time import sleep

numero = int(input("Insira um valor: "))

def contagem_regressiva(numero):
    if numero <= 0:
        print("O valor deve ser positivo!")
    while numero > 0:
        print("{:.1f}".format(numero))
        sleep(0.1)
        numero -= 0.1
    return numero

contagem_regressiva(numero)