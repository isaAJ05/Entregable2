print("Bienvenidx")
print("Portafolio de máximo beneficio")
while True:
    correlacion_maxima = float(input("Ingrese la correlación máxima permitida (-1 a 1): "))
    if -1 <= correlacion_maxima <= 1:
        break
    else:
        print("Por favor, ingrese un valor entre -1 y 1.")
while True:
    acciones_minimas = input("Número mínimo de acciones deseadas en el portafolio: ")
    try:
        acciones_minimas = int(acciones_minimas)
        break
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
with open('correlaciones.txt', 'r') as file:
    primera_linea = file.readline().strip()
    try:
        acciones_minimas = int(primera_linea)
    except ValueError:
        print("El valor en la primera línea de correlaciones.txt no es un número entero válido.")
        exit(1)