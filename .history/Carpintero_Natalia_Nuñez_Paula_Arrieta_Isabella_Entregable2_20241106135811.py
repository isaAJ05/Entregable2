import itertools
import networkx as nx
import matplotlib.pyplot as plt
# Crear el grafo
G = nx.Graph()
with open('correlaciones.txt', 'r') as file:
    file.readline()  # saltar la primera línea que contiene el total de acciones
    for line in file.readlines():
        parts = line.split()
        if len(parts) == 3:
            accion1 = parts[0]
            accion2 = parts[1]
            correlacion = float(parts[2])
            G.add_edge(accion1, accion2, weight=correlacion)
# Dibujar el grafo
pos = nx.spring_layout(G)  # layout para una mejor visualización
edges = G.edges(data=True)
weights = [edge[2]['weight'] for edge in edges]

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d["weight"]:.2f}' for u, v, d in edges})
nx.draw_networkx_edges(G, pos, width=weights)

plt.title("Grafo de Correlaciones entre Acciones")
plt.show()

print("Bienvenidx")
print("Portafolio de máximo beneficio")


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
    print(acciones_minimas, correlacion_maxima )

def portafolio_riesgo_controlado():
    # Aquí iría la lógica para el portafolio con riesgo controlado
    print("Función para calcular el portafolio con riesgo controlado aún no implementada.")

while True:
    print("Bienvenidx")
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
        print("Saliendo del programa.")
        break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()

