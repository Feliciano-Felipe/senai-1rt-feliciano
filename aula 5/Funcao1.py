largura = float(input("Insira o valor da largura: "))
comprimento = float(input("Insira o valor do comprimento: "))

def area(largura, comprimento):
    total = largura * comprimento
    return total

print("Área:",area(largura, comprimento))