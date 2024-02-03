print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Círculo")
print("5. Rombo")
print("6. Trapecio")
print("7. Salir")
opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    lado = float(input("Ingrese la longitud del lado: "))
    area = lado * lado
    print(f"El área del cuadrado es: {area}")
elif opcion == 2:
    base = float(input("Ingrese la longitud de la base: "))
    altura = float(input("Ingrese la longitud de la altura: "))
    area = base * altura
    print(f"El área del rectángulo es: {area}")
elif opcion == 3:
    lado1 = float(input("Ingrese la longitud del primer lado: "))
    lado2 = float(input("Ingrese la longitud del segundo lado: "))
    altura = float(input("Ingrese la longitud de la altura: "))
    area = (lado1 * lado2) / 2
    print(f"El área del triángulo es: {area}")
elif opcion == 4:
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.14159 * radio * radio
    print(f"El área del círculo es: {area}")
elif opcion == 5:
    diagonal1 = float(input("Ingrese la longitud de la diagonal 1: "))
    diagonal2 = float(input("Ingrese la longitud de la diagonal 2: "))
    area = (diagonal1 * diagonal2) / 2  
    print(f"El área del rombo es: {area}")
elif opcion == 6:
    base1 = float(input("Ingrese la longitud de la base mayor: "))
    base2 = float(input("Ingrese la longitud de la base menor: "))
    altura = float(input("Ingrese la longitud de la altura: "))
    area = ((base1 + base2) / 2) * altura
    print(f"El área del trapecio es: {area}")
elif opcion == 7:
    print("Saliendo del programa...")
else:
    print("Opción inválida. Por favor, seleccione una opción del menú.")
print("Gracias por utilizar el programa de cálculo de áreas.")
