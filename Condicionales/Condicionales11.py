
tamanios_pizza = {1: 15000, 2: 24000, 3: 36000}
precio_ingrediente_adicional = 4000

tamanio_pizza = int(input("Ingrese el tamaño de la pizza (1, 2 o 3): "))
ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales: "))

if tamanio_pizza not in tamanios_pizza:
    print("Tamaño de pizza no válido. Seleccione un tamaño válido (1, 2 o 3).")
    exit()

precio_base = tamanios_pizza[tamanio_pizza]


precio_total = precio_base + (ingredientes_adicionales * precio_ingrediente_adicional)

print(f"El precio total a pagar por la pizza de tamaño {tamanio_pizza} con {ingredientes_adicionales} ingredientes adicionales es: ${precio_total}")
