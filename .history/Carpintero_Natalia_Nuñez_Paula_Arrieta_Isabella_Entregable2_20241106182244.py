import itertools
import networkx as nx
import matplotlib.pyplot as plt


def portafolio_maximo_beneficio(correlacion_maxima, acciones_minimas):
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
            print("Esto es subset (combinando 3 en este caso)", subset)
            grafito = Grafo_General.subgraph(subset) #subgrafo con las acciones seleccionadas
            es_valido = True
            for u, v in grafito.edges: #para cada arista en el subgrafo (osea para cada acción)
                if abs(grafito[u][v]['weight']) > correlacion_maxima: #se verifica  si la correalcion es mayor a la maxima (ES COMO EL COMPLEMENTO)
                    es_valido = False
                    break
            if es_valido: # si la correlacion es menor o igual a la maxima es valido
                print("Esto es una accion valida porque es menor o igual a la correlacion maxima", subset)
                portafolios_validos.append(subset)
    
    if not portafolios_validos:
        print("No se encontraron portafolios que cumplan con las restricciones dadas.")
        return
    # Encontrar el portafolio con el rendimiento promedio máximo 
    max_rendimiento_promedio = 0
    for portafolio in portafolios_validos: #para cada portafolio valido (lista de acciones)
        rendimiento_total = 0
        for accion in portafolio: #para cada accion en el portafolio
            rendimiento_total += rendimientos[accion] #se suma el rendimiento de cada accion, de acuerdo a lo extraido en el txt
            rendimiento_promedio = rendimiento_total / len(portafolio) # se va promediando el rendimiento de cada accion (su acumulado)
            mejor_portafolio = portafolio #asumimos que el mejor portafolio es el primero
            #max_rendimiento_promedio = rendimiento_promedio #asumimos que el mejor rendimiento promedio es el primero para ir comparando entre los diversos portafolios
        print(f"Portafolio {portafolio} con rendimiento promedio {rendimiento_promedio}")
        if rendimiento_promedio > max_rendimiento_promedio:
            max_rendimiento_promedio = rendimiento_promedio
            mejor_portafolio = portafolio
    return mejor_portafolio, max_rendimiento_promedio, portafolios_validos        
    
    
def portafolio_riesgo_controlado():
    # Leer rendimientos de las acciones
    rendimientos_riesgo = {}
    with open('rendimientos.txt', 'r') as file:
        for line in file.readlines():
            parts = line.split()
            if len(parts) == 3:
                accion = parts[0]
                rendimiento = float(parts[1])
                riesgo = float(parts[2])
                rendimientos_riesgo[accion] = (rendimiento, riesgo)
    print(rendimientos_riesgo)

def Dibujar_Grafo(G):
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=3000, node_color='lightblue')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
def Mostrar_Grafo(G):
    for edge in G.edges(data=True):
        print(f"{edge[0]} - {edge[1]}: {edge[2]['weight']}")


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
        mejor_portafolio, max_rendimiento_promedio, portafolios_validos= portafolio_maximo_beneficio(correlacion_maxima, acciones_minimas)
        # Mostrar resultados
        print(f"Mejor portafolio: {mejor_portafolio}")
        print(f"Rendimiento promedio del mejor portafolio: {max_rendimiento_promedio}")
        print(f"Número total de portafolios válidos: {len(portafolios_validos)}")
        print(f"Portafolios válidos: {portafolios_validos}")
        print("\n")
    elif opcion == '2':
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
    while True:
        riesgo_promedio_max = float(input("Ingrese el valor de riesgo promedio maximo de las acciones deseado: "))
        if 1 <= riesgo_promedio_max <= 10:
            break
        else:
            print("Por favor, ingrese un valor entre 1 y 10.")
    print(f"Acciones mínimas: {acciones_minimas}\nCorrelación máxima: {correlacion_maxima} \nRiesgo promedio: {riesgo_promedio_max}")
        portafolio_riesgo_controlado()
    elif opcion == '3':
        print("Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")



