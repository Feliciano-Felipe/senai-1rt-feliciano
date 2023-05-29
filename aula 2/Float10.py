idade = int(input("Digite a sua idade: "))

from datetime import date
ano_atual = date.today().year

ano_futura = ano_atual + (100 - idade)

print("Você fará 100 anos em", ano_futura)
