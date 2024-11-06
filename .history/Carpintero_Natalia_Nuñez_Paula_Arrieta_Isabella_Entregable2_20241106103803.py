print("Bienvenidx")
print("Portafolio de máximo beneficio")
while True:
    correlacion_maxima = float(input("Ingrese la correlación máxima permitida (-1 a 1): "))
    if -1 <= correlacion_maxima <= 1:
        break
    else:
        print("Por favor, ingrese un valor entre -1 y 1.")
with open('correlaciones.txt', 'r') as file:
    total_acciones = int(file.readline().strip())
while True:
    acciones_minimas = int(input("Número mínimo de acciones deseadas en el portafolio: "))
    if 0 <= acciones_minimas <= total_acciones:
        break
    else:
        print(f"Por favor, ingrese un valor entre 0 y {total_acciones}.")
print(acciones_minimas, correlacion_maxima )
with open('rendimientos.txt', 'r') as file:
    rendimientos = [float(line.split()[1]) for line in file.readlines()]
rendimientos.sort(reverse=True)
mejores_rendimientos = rendimientos[:acciones_minimas]

print("Los mejores rendimientos son:", mejores_rendimientos)