frase = input("Ingrese la frase: ")

frase_procesada = frase.lower().replace(" ", "")


frase_invertida = frase_procesada[::-1]

print("Frase original:", frase)
print("Frase sin espacios y en minúsculas:", frase_procesada)
print("Frase invertida:", frase_invertida)

if frase_procesada == frase_invertida:
    print("La frase o palabra es un palíndromo")
else:
    print("La frase o palabra no es un palíndromo")
