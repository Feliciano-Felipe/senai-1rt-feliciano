nota = float(input("Insira a sua nota na competição: "))

if nota < 50:
    print("Você ganhou um Certificado de Participação")
elif nota < 60:
    print ("Você ganhou um Certificado de Menção de Honrosa")
elif nota < 70:
    print ("Você ganhou uma Medalha de Bronze")
elif nota < 90:
    print ("Você ganhou uma Medalha de Prata")
else:
    print ("Você ganhou uma Medalha de Ouro")