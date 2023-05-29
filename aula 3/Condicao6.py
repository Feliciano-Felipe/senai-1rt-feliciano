vel = float(input("Informe a velocidade: "))

velex = vel - 80
multa = velex * 7

if vel > 80:
    print("Você foi multado")
    print("Valor da multa: R$",multa)
else:
    print("Abaixo do limite. Continue assim")