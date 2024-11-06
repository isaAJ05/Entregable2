import itertools
import networkx as nx
import matplotlib.pyplot as plt


def portafolio_maximo_beneficio():
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
    print(f"Acciones mínimas: {acciones_minimas}\nCorrelación máxima: {correlacion_maxima}")
    
    # Leer rendimientos de las acciones
    rendimientos = {}
    with open('rendimientos.txt', 'r') as file:
        for line in file.readlines():
            parts = line.split()
            if len(parts) == 3:
                accion = parts[0]
                rendimiento = float(parts[1])
                rendimientos[accion] = rendimiento
    print(rendimientos)
    
    acciones = list(Grafo_General.nodes) #Nodos del grafo son las acciones
    portafolios_validos = [] # portafolios que cumplen con las condiciones osea que la correlacion sea menor a la maxima
    for i in range(acciones_minimas, len(acciones) + 1): #desde las acciones minimas hasta el total de acciones
        for subset in itertools.combinations(acciones, i): # hacer combinaciones de las acciones
            print("Esto es subset ", subset)
            grafito = Grafo_General.subgraph(subset) #nuevo grafo con las acciones seleccionadas
            if all(abs(grafito[u][v]['weight']) <= correlacion_maxima for u, v in grafito.edges):
                print("Esto es grafito ", grafito)
                portafolios_validos.append(subset)
    
    if not portafolios_validos:
        print("No se encontraron portafolios que cumplan con las restricciones dadas.")
        return
    # Encontrar el portafolio con el rendimiento promedio máximo
    mejor_portafolio = None
    max_rendimiento_promedio = -float('inf')
    for portafolio in portafolios_validos:
        rendimiento_promedio = sum(rendimientos[accion] for accion in portafolio) / len(portafolio)
        if rendimiento_promedio > max_rendimiento_promedio:
            max_rendimiento_promedio = rendimiento_promedio
            mejor_portafolio = portafolio

    # Mostrar resultados
    print(f"Mejor portafolio: {mejor_portafolio}")
    print(f"Rendimiento promedio del mejor portafolio: {max_rendimiento_promedio}")
    print(f"Número total de portafolios válidos: {len(portafolios_validos)}")

    Dibujar_Grafo(Grafo_General.subgraph(mejor_portafolio))
    
def portafolio_riesgo_controlado():
    # Aquí iría la lógica para el portafolio con riesgo controlado
    print("Función para calcular el portafolio con riesgo controlado aún no implementada.")

def Dibujar_Grafo(G):
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=3000, node_color='lightblue')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
# Crear el grafo
Grafo_General = nx.Graph()
with open('correlaciones.txt', 'r') as file:
    file.readline()  # saltar la primera línea que contiene el total de acciones
    for line in file.readlines():
        parts = line.split()
        if len(parts) == 3:
            accion1 = parts[0]
            accion2 = parts[1]
            correlacion = float(parts[2])
            Grafo_General.add_edge(accion1, accion2, weight=correlacion)
    #Dibujar_Grafo(Grafo_General)

while True:
    print("Bienvenidx al programa!")
    print("\nMenú de Opciones:")
    print("1. Portafolio de máximo beneficio")
    print("2. Portafolio con riesgo controlado")
    print("3. Salir")
    opcion = input("Seleccione una opción (1, 2, 3): ")
        
    if opcion == '1':
        portafolio_maximo_beneficio()
    elif opcion == '2':
        portafolio_riesgo_controlado()
    elif opcion == '3':
        print("Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")



