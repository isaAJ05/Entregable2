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
    rendimientos = []
    for line in file.readlines():
        parts = line.split() # separa la línea en palabras
        acciones = parts[0] # la primera palabra es la acción
        rendimiento = float(parts[1])
        rendimientos.append((acciones, rendimiento))

rendimientos.sort(key=lambda x: x[1], reverse=True)
mejores_rendimientos = rendimientos[:acciones_minimas]

print("Los mejores rendimientos son:")
for nombre, rendimiento in mejores_rendimientos:
    print(f"{nombre}: {rendimiento}")