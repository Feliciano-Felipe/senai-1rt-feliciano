num1 = float(input("Insira o valor 1: "))
num2 = float(input("Insira o valor 2: "))
num3 = float(input("Insira o valor 3: "))

def maior(num1,num2,num3):
    resultado = max(num1,num2,num3)
    return resultado

print("O maior número é",maior(num1,num2,num3))