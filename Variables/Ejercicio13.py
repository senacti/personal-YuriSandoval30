segundos = int(input("Ingrese el tiempo en segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60

print(f"{segundos} segundos son {horas} horas y {minutos} minutos.")
