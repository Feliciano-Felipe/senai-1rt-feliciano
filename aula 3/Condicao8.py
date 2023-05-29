numero1 = float(input("Insira um valor: "))
numero2 = float(input("Insira outro valor: "))
operador = input("Selecione o operador: ")

if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
else:
    operador == "/"
    resultado = numero1 / numero2

print(resultado)