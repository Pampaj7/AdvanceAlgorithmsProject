from matplotlib import pyplot as plt

"""
# Create graph
G = nx.fast_gnp_random_graph(10, 0.3)

# Pick a random node
source = random.choice(list(G.nodes))

# Find the longest shortest path from the node
shortest_paths = nx.shortest_path(G, source=source)  # <- uses shortest path instead of 2 bfs!!
target = max(shortest_paths, key=lambda i: len(shortest_paths[i]))
l_s_path = shortest_paths[target]
l_s_path_edges = list(zip(l_s_path, l_s_path[1:]))

# Draw the graph, then draw over the required edges in red.
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)
nx.draw_networkx_edges(G, edge_color='r', edgelist=l_s_path_edges, pos=pos)
plt.show()
"""

import networkx as nx
from collections import deque


def calcola_diametro_grafo(grafo):
    diametro = 0

    for nodo in grafo.nodes():
        distanze = {nodo: 0}
        coda = deque([nodo])

        while coda:
            u = coda.popleft()

            for v in grafo[u]:
                if v not in distanze:
                    distanze[v] = distanze[u] + 1
                    coda.append(v)

        max_distanza = max(distanze.values())
        diametro = max(diametro, max_distanza)

    return diametro


# Esempio di utilizzo
grafo = nx.fast_gnp_random_graph(100, 1)

diametro_grafo = calcola_diametro_grafo(grafo)
print("Il diametro del grafo è tramite il nostro codice è:", diametro_grafo)

diametro_grafo = nx.diameter(grafo)
print("Il diametro del grafo è:", diametro_grafo)
