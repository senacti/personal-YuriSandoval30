salario_diario = float(input("Ingrese el salario diario del empleado: "))
dias_trabajados = int(input("Ingrese el número de días trabajados: "))

salario_bruto = salario_diario * dias_trabajados
pension = salario_bruto * 0.10
salud = salario_bruto * 0.15
salario_neto = salario_bruto - pension - salud

print(f"Salario bruto: ${salario_bruto:}")
print(f"Descuento por pensión (10%): ${pension:}")
print(f"Descuento por salud (15%): ${salud:}")
print(f"Salario neto a pagar: ${salario_neto:}")
