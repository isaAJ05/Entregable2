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
    acciones = list(Grafo_General.nodes) #Nodos del grafo son las acciones
    portafolios_validos = [] # portafolios que cumplen con las condiciones osea que la correlacion sea menor a la maxima
    for i in range(acciones_minimas, len(acciones) + 1): #desde las acciones minimas hasta el total de acciones
        for subset in itertools.combinations(acciones, i): # hacer combinaciones de las acciones
            Nuevo_Grafo = Grafo_General.subgraph(subset) #nuevo grafo con las acciones seleccionadas
            if all(abs(Nuevo_Grafo[u][v]['weight']) <= correlacion_maxima for u, v in Nuevo_Grafo.edges):
                portafolios_validos.append(subset)
    
    if not portafolios_validos:
        print("No se encontraron portafolios que cumplan con las restricciones dadas.")
        return
    Dibujar_Grafo(Nuevo_Grafo)
    """""
    mejor_portafolio = max(portafolios_validos, key=lambda p: sum(Grafo_General.nodes[n]['rendimiento'] for n in p) / len(p))
    rendimiento_promedio = sum(Grafo_General.nodes[n]['rendimiento'] for n in mejor_portafolio) / len(mejor_portafolio)
    
    print("Portafolio de máximo beneficio encontrado:")
    print("Acciones en el portafolio:", mejor_portafolio)
    print("Rendimiento promedio del portafolio:", rendimiento_promedio)
    print("Número total de portafolios posibles que cumplen con la restricción:", len(portafolios_validos))
"""""
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



