
monto_cuenta = float(input("Ingrese el monto de la cuenta: "))

if monto_cuenta < 150000:
    metodo_pago = "Efectivo"
elif 150000 <= monto_cuenta <= 300000:
    metodo_pago = "Celular (dinero electrónico)"
elif 300000 < monto_cuenta <= 600000:
    metodo_pago = "Tarjeta de débito"
else:
    metodo_pago = "Tarjeta de crédito"

print(f"Se ha seleccionado el método de pago: {metodo_pago}")
