from matplotlib import pyplot as plt
import networkx as nx
import random
import ProgressionBar as pb
from collections import deque

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


def calcola_diametro_grafo(graph):
    # Ottieni le componenti connesse del grafo
    connected_components = nx.connected_components(graph)
    diameterList = []
    for component in connected_components:
        # Crea il sottografo della componente corrente
        subgraph = graph.subgraph(component)  # merda fumante

        diameter = nx.diameter(subgraph)
        diameterList.append(diameter)
    return diameterList


def approximate_diameter(graph, sample_size=1000, max_hops=100):
    nodes = list(graph.nodes())
    diameter = 0

    # Select random nodes as starting points for sampling
    sample_nodes = random.sample(nodes, min(sample_size, len(nodes)))

    for node in sample_nodes:
        visited = set([node])
        queue = [(node, 0)]

        while queue:
            current_node, hops = queue.pop(0)

            if hops > max_hops:
                break

            neighbors = list(graph.neighbors(current_node))

            if not neighbors:
                continue

            # Select a random neighbor and add it to the visited set
            random_neighbor = random.choice(neighbors)
            visited.add(random_neighbor)

            # Add the random neighbor to the queue for further exploration
            queue.append((random_neighbor, hops + 1))

        # Update the diameter if necessary
        diameter = max(diameter, hops)

    return diameter


"""
# lower bound

# idea: fare 2 bfs, la prima su un random node r, la seconda su x nodo + distante da r
# ripetere bfs su x e cerco y, nodo più distante da x il lower bound è la distanza tra x e y
# il metodo deve ritronare la distanza tra r e x, la seconda volta tra x e y

# upper bound

# eccentricità dei rimanenti nodi, se i nodi hanno eccentricità minore del lower bound <- usare ecc method di networkx?


def degreeTree(G):
    return [n for n, d in G.in_degree() if d == 0]


def lower_bound(G):
    source = random.choice(list(G.nodes))
    treeRX = nx.bfs_tree(G, source=source)  # return a tree, not height
    distRX = calcola_altezza_Albero(treeRX)
    # come prendo nodo più distante?


def calcola_altezza_albero(grafo):
    # nodo_radice = degreeTree(grafo)
    nodo_radice = random.choice(list(grafo.nodes))

    # Dizionario per tenere traccia dei livelli dei nodi
    livelli = {nodo: -1 for nodo in grafo}  # TODO debug
    x = nodo_radice
    # Inizializza il livello del nodo radice a 0
    livelli[nodo_radice] = 0

    # Coda per la visita in ampiezza
    coda = deque()
    coda.append(nodo_radice)

    # Altezza massima del grafo
    altezza = 0

    while coda:  # gucci
        last_node = coda[-1]
        nodo = coda.popleft()  # cazzo è

        # Trova i nodi adiacenti al nodo corrente
        for adiacente in grafo[nodo]:
            if livelli[adiacente] == -1:
                # Se il nodo adiacente non è stato visitato, assegna il livello corrente + 1
                livelli[adiacente] = livelli[nodo] + 1
                coda.append(adiacente)
                # x = coda[-1]
                # Aggiorna l'altezza massima del grafo se necessario
                altezza = max(altezza, livelli[adiacente])

    return altezza, last_node


# Esempio di utilizzo
grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D', 'C'],
    'C': ['A', 'E', 'B'],
    'D': ['B', 'A', 'E'],
    'E': ['C', 'F', 'D'],
    'F': ['E']
}

nodo_radice = 'A'

altezza_albero, x = calcola_altezza_albero(grafo)
print("L'altezza del grafo è:", altezza_albero)
print('Ultimo nodo è: '+x)
"""


def max_Ecc(G):  # troppo costoso
    s_dict = nx.eccentricity(G)

    max_value = max(s_dict.items(), key=lambda x: x[1])
    max_index = max_value[0]
    max_eccentricity = max_value[1]

    print("Nodo con eccentricità max:", max_index)
    print("Valore di eccentricità max:", max_eccentricity)
    return max_index, max_eccentricity


def lower_Bound(G):
    source = random.choice(list(G.nodes))

    max_value = min(nx.eccentricity(G), key=nx.eccentricity(G).get)  # qui si bugga
    print('ecc ', max_value)
    treeRX = nx.bfs_tree(G, source=source)
    distRX, x = calcola_altezza_Albero(treeRX, nodo_radice=source)
    print('source: ', source)

    # Trova il nodo più distante da x nel sottografo rimanente
    # treeXY = nx.bfs_tree(G.subgraph(treeRX.nodes - [x]), source=x)
    treeXY = nx.bfs_tree(G, source=x)
    print('x: ', x)
    print()

    distXY, y = calcola_altezza_Albero(treeXY, nodo_radice=x)
    print('distanza: ', distRX)
    print('ultimo elemento: ', x)
    lower_bound = distRX + distXY

    return lower_bound


def calcola_altezza_Albero(grafo, nodo_radice):
    # Dizionario per tenere traccia dei livelli dei nodi
    livelli = {nodo: -1 for nodo in grafo}
    livelli[nodo_radice] = 0

    # Variabili per tenere traccia del nodo con l'altezza massima
    altezza_massima = 0
    nodo_altezza_massima = None

    # Stack per la visita in profondità
    stack = [nodo_radice]

    while stack:
        nodo = stack.pop()

        for adiacente in grafo[nodo]:
            if livelli[adiacente] == -1:
                livelli[adiacente] = livelli[nodo] + 1
                stack.append(adiacente)

                # Aggiorna il nodo con l'altezza massima se necessario
                if livelli[adiacente] > altezza_massima:
                    altezza_massima = livelli[adiacente]
                    nodo_altezza_massima = adiacente

    return altezza_massima  # , nodo_altezza_massim

import networkx as nx
from collections import deque

# Crea un grafo di esempio
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])

# Funzione per trovare il nodo più distante da un nodo di partenza utilizzando BFS
def farthest_node_bfs(graph, start_node = nx.utils.random.choice(list(G.nodes()))):
    # Inizializza la coda della BFS
    queue = deque([(start_node, 0)])  # (nodo, distanza)

    # Inizializza un insieme per tenere traccia dei nodi visitati
    visited = set([start_node])

    # Variabile per tenere traccia del nodo più distante
    farthest_node = start_node
    max_distance = 0

    while queue:
        current_node, distance = queue.popleft()

        if distance > max_distance:
            # Aggiorna il nodo più distante
            farthest_node = current_node
            max_distance = distance

        # Esplora i nodi adiacenti
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)

    return farthest_node, max_distance

# Nodo di partenza
start_node = 1

def my_eccentricity(graph, node):
    node, distance = farthest_node_bfs(graph=graph, start_node=node)
    return distance

import networkx as nx

# Crea un grafo di esempio
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8)])

# Funzione per trovare l'insieme di nodi distanti "i" da un nodo di partenza "a"
def Fiu(graph, distance, start_node = nx.utils.random.choice(list(G.nodes()))):
    visited = set()  # Insieme per tenere traccia dei nodi visitati
    current_level = {start_node}  # Insieme di nodi al livello corrente

    for _ in range(distance):
        next_level = set()  # Insieme di nodi al prossimo livello

        # Espandi il livello corrente
        for node in current_level:
            visited.add(node)  # Aggiungi il nodo visitato
            neighbors = set(graph.neighbors(node))
            next_level.update(neighbors - visited)

        current_level = next_level

    return current_level

# Nodo di partenza
start_node = 1

# Distanza "i"
distance = 2

# Trova l'insieme di nodi distanti "i" dal nodo di partenza utilizzando BFS
nodes = nodes_at_distance(G, start_node, distance)

# Stampa l'insieme di nodi
print("Nodi a distanza", distance, "dal nodo", start_node, ":", nodes)



def iFUB(graph, node):
    fringe = nx.periphery(graph)  # cerco la frangia del grafo
    subgraph = graph.subgraph(fringe)  # la metto in un sottografo
    s_dict = nx.eccentricity(graph)  # così posso prendere le eccentricità dei nodi della sola frangia
    i = s_dict[node]  # cerco l'eccentricità del nodo che gli deve essere passato?
    lb = i  # inizializzo il lower bound
    ub = 2 * i  # inizializzo l'upperbound
    bi = max_Ecc(subgraph)  # in teoria è un buond a sua volta
    while ub > lb:  # cerco l'ottimo
        if max(lb, bi > 2 * i - 1):  # maggia nera
            return max(lb)
        else:  # aggiornamento delle variabili
            lb = max(lb, bi)  # ma perché???
            ub = 2 * (i - 1)
            i -= 1
    return lb


# Esempio di utilizzo
"""grafo = nx.fast_gnp_random_graph(20, 0.9)

altmax, nodmax = calcola_altezza_Albero(
    grafo, random.choice(list(grafo.nodes)))
print('altezza max: ', altmax, 'nodo + distante: ', nodmax)

print('lower bound: ', lower_Bound(grafo))

print('upper bound: ', nx.eccentricity(grafo))  # TODO finire

print(nx.eccentricity(grafo).values())"""
