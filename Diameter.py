import networkx as nx
import random
from collections import deque
from tqdm import tqdm

def calcola_diametro_grafo(graph):
    # Ottieni le componenti connesse del grafo
    connected_components = nx.connected_components(graph)  # era qui che faceva le componeneti connesse
    diameterList = []
    for component in connected_components:
        # Crea il sottografo della componente corrente
        subgraph = graph.subgraph(component)  # merda fumante

        diameter = nx.diameter(subgraph)
        diameterList.append(diameter)
    return diameterList


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


# ritorna il nodo di max grco per ottimizzare calcolo esatto del diametro
def findMaxDegreeNodeGraph(graph):
    max_deg = 0
    max_deg_node = None
    for node in graph.nodes():
        if max_deg < graph.degree(node):
            max_deg = graph.degree(node)
            max_deg_node = node
    return max_deg_node


# Funzione per trovare il nodo più distante da un nodo di partenza utilizzando BFS
def farthest_node_bfs(graph, start_node=None):  # oro
    if start_node is None:  # il metodo trova l'eccentricità
        start_node = random.choice(list(graph.nodes()))

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


# ritorna la fringe radicata in start a distanza maxdepth
# viene usata bfs per abbattere il costo computazionale
def bfs_maxdepth(graph, maxdepth, start):
    queue = deque([start])
    depths = {start: 0}
    maxdepth_nodes = []

    while queue:
        vertex = queue.popleft()
        if depths[vertex] == maxdepth:
            maxdepth_nodes.append(vertex)
            continue

        for neighbour in graph[vertex]:
            if neighbour in depths:
                continue
            queue.append(neighbour)
            depths[neighbour] = depths[vertex] + 1

    return maxdepth_nodes


def Biu(graph, level, node):
    max_ecc = 0
    nodes = bfs_maxdepth(graph, level, node)
    progress_bar = tqdm(nodes, desc="Processing nodes", leave=False)

    for node in progress_bar:
        _, ecc = farthest_node_bfs(graph, start_node=node)
        if ecc > max_ecc:
            max_ecc = ecc
        progress_bar.set_postfix({"Max Eccentricity": max_ecc})
    return max_ecc

# TODO implementare 2-swep
