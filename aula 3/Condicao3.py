salario = float(input("informe o seu salário: "))

aumento10 = salario + (salario * 0.10)
aumento15 = salario + (salario * 0.15)

if salario > 8250.00:
    print("Seu novo salário: R$",aumento10)
else:
    print("Seu novo salário: R$",aumento15)