import matplotlib.pyplot as plt
import networkx as nx
import random

"""
# Create graph
G = nx.fast_gnp_random_graph(10, 0.3)

# Pick a random node
source = random.choice(list(G.nodes))

# Find the longest shortest path from the node
shortest_paths = nx.shortest_path(G, source=source)
target = max(shortest_paths, key=lambda i: len(shortest_paths[i]))
l_s_path = shortest_paths[target]
l_s_path_edges = list(zip(l_s_path, l_s_path[1:]))

# Draw the graph, then draw over the required edges in red.
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)
nx.draw_networkx_edges(G, edge_color='r', edgelist=l_s_path_edges, pos=pos)
plt.show()
"""


#####################  WARSHALL ################
def calcola_diametro_grafo(grafo):
    distanze = {}  # Dizionario per memorizzare le distanze tra i nodi

    # Inizializza la matrice delle distanze con valore infinito per tutte le coppie di nodi
    for u in grafo.nodes():
        distanze[u] = {}
        for v in grafo.nodes():
            if u == v:
                distanze[u][v] = 0
            else:
                distanze[u][v] = float('inf')

    # Aggiorna le distanze tra i nodi adiacenti nel grafo
    for u, v in grafo.edges():
        distanze[u][v] = 1
        distanze[v][u] = 1

    # Calcola le distanze minime tra tutte le coppie di nodi utilizzando l'algoritmo di Floyd-Warshall
    for k in grafo.nodes():
        for u in grafo.nodes():
            for v in grafo.nodes():
                distanze[u][v] = min(distanze[u][v], distanze[u][k] + distanze[k][v])

    # Trova la distanza massima tra tutte le coppie di nodi nel grafo
    diametro = 0
    for u in grafo.nodes():
        for v in grafo.nodes():
            if distanze[u][v] != float('inf'):
                diametro = max(diametro, distanze[u][v])

    return diametro


# Esempio di utilizzo
grafo = nx.Graph()
grafo.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

diametro_grafo = calcola_diametro_grafo(grafo)
print("Il diametro del grafo è:", diametro_grafo)
