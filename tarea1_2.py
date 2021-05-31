frase = str(input("Ingrese cualquier frase sin acentos: ")).lower().replace(" ", "")
if frase == frase [::-1]:
    print("La frase: " + " " + frase + " " + "es un palíndromo")
else:
    print("La frase que escribio no es un palíndromo")