km = float(input("Informe a distância da viagem em km: "))

preco050 = km * 0.50
preco045 = km * 0.45

if km > 200:
    print("Preço:",preco045,"km")
else:
    print("Preço:",preco050,"km")