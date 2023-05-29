numero = int(input("Digite um número inteiro: "))

fatorial = 1
contador = 1

if numero < 0:
    print("O fatorial não pode ser calculado para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    while contador <= numero:
        fatorial *= contador
        contador += 1
    
    print(f"O fatorial de {numero} é {fatorial}.")
