def verificar_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

numeros = [3, 10, 7, 16, 22]

for num in numeros:
    if verificar_par(num):
        print(num, "é par.")
    else:
        print(num, "não é par.")
