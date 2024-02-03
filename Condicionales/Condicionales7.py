print("Menu de Conversion de Temperaturas")
print("1. Fahrenheit")
print("2. Celsius")
print("3. Kelvin")
print("4. Rankine")
print("5. Réaumur")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    rankine = fahrenheit + 459.67
    reaumur = (fahrenheit - 32) * 4/9
    print("Temperatura en Celsius:", celsius)
    print("Temperatura en Kelvin:", kelvin)
    print("Temperatura en Rankine:", rankine)
    print("Temperatura en Réaumur:", reaumur)

elif opcion == 2:
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    rankine = (celsius * 9/5) + 491.67
    reaumur = celsius * 4/5
    print("Temperatura en Fahrenheit:", fahrenheit)
    print("Temperatura en Kelvin:", kelvin)
    print("Temperatura en Rankine:", rankine)
    print("Temperatura en Réaumur:", reaumur)

elif opcion == 3:
    kelvin = float(input("Ingrese la temperatura en Kelvin: "))
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    rankine = kelvin * 9/5
    reaumur = (kelvin - 273.15) * 4/5
    print("Temperatura en Celsius:", celsius)
    print("Temperatura en Fahrenheit:", fahrenheit)
    print("Temperatura en Rankine:", rankine)
    print("Temperatura en Réaumur:", reaumur)

elif opcion == 4:
    rankine = float(input("Ingrese la temperatura en Rankine: "))
    celsius = (rankine - 491.67) * 5/9
    fahrenheit = rankine - 459.67
    kelvin = rankine * 5/9
    reaumur = (rankine - 491.67) * 4/9
    print("Temperatura en Celsius:", celsius)
    print("Temperatura en Fahrenheit:", fahrenheit)
    print("Temperatura en Kelvin:", kelvin)
    print("Temperatura en Réaumur:", reaumur)

elif opcion == 5:
    reaumur = float(input("Ingrese la temperatura en Réaumur: "))
    celsius = reaumur * 5/4
    fahrenheit = (reaumur * 9/4) + 32
    kelvin = (reaumur * 5/4) + 273.15
    rankine = (reaumur * 9/4) + 491.67
    print("Temperatura en Celsius:", celsius)
    print("Temperatura en Fahrenheit:", fahrenheit)
    print("Temperatura en Kelvin:", kelvin)
    print("Temperatura en Rankine:", rankine)

else:
    print("Opción inválida")