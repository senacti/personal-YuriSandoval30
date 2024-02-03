nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 0 or edad > 100:
    print("Por favor, ingrese una edad válida.")
else:
    if edad >= 18:
        print(f"Hola {nombre}, usted es mayor de edad.")
    else:
        print(f"Hola {nombre}, usted es menor de edad.")
