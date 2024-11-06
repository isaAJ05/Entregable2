import itertools

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
# Leer las correlaciones de las acciones
correlaciones = {}
with open('correlaciones.txt', 'r') as file:
    file.readline()  # saltar la primera línea que contiene el total de acciones
    for line in file.readlines():
        parts = line.split()
        if len(parts) == 3:
            accion1 = parts[0]
            accion2 = parts[1]
            correlacion = float(parts[2])
            correlaciones[(accion1, accion2)] = correlacion  # guardar la correlación entre las acciones
            correlaciones[(accion2, accion1)] = correlacion  # guardar la correlación entre las acciones
print(correlaciones)
for i in range(len(correlaciones)):
    if correlaciones.get > correlacion_maxima:
        correlaciones.pop(i)
print(correlaciones)
"""""
with open('rendimientos.txt', 'r') as file:
    rendimientos = []
    for line in file.readlines():
        parts = line.split() # separa la línea en palabras
        acciones = parts[0] # la primera palabra es la acción
        rendimiento = float(parts[1])
        rendimientos.append((acciones, rendimiento))

rendimientos.sort(key=lambda x: x[1], reverse=True) # ordena de mayor a menor rendimiento
mejores_rendimientos = rendimientos[:acciones_minimas] # selecciona las acciones con los mejores rendimientos de acuerdo al número mínimo de acciones deseadas
rendimiento_max=0
for i in range(len(mejores_rendimientos)):
    rendimiento_max+=mejores_rendimientos[i][1]
rendimiento_max/=acciones_minimas

print("Los mejores rendimientos son:")
for acciones, rendimiento in mejores_rendimientos:
    print(f"{acciones}: {rendimiento}")
print(f"El rendimiento promedio máximo es: {rendimiento_max}")
"""""

