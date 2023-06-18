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


# ritorna il nodo di max grco per ottimizzare calcolo esatto del diametro
def findMaxDegreeNodeGraph(graph):
    max_deg = 0
    max_deg_node = None
    for node in graph.nodes():
        if max_deg < graph.degree(node):
            max_deg = graph.degree(node)
            max_deg_node = node
    return max_deg_node


def bfs_livelli(graph):  # ritrona la fringe, calcola da solo il nodo con massimo grado
    start_node = findMaxDegreeNodeGraph(graph)
    print('il nodo di massima centralità è: ', start_node)
    visited = set()
    last_level = {}

    queue = deque([(start_node, 0)])
    livello_massimo = -1
    livelli = {start_node: 0}

    while queue:
        node, level = queue.popleft()
        if node not in visited:
            # print(node)
            visited.add(node)
            neighbors = graph.neighbors(node)

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))
                    livelli[neighbor] = level + 1
                    if level > livello_massimo and neighbor not in last_level:
                        livello_massimo = level
                        # print('livello max aggiornato, inserisco il nodo: ',neighbor)
                        last_level = {neighbor: 0}
                    elif level == livello_massimo and neighbor not in last_level:
                        # print('inserisco il nodo: ', neighbor)
                        last_level[neighbor] = 0

    print('larghezza fringe: ', len(last_level.keys()))
    return livello_massimo, last_level.keys()


def eccentricity(graph, root):
    visited = set()  # Insieme dei nodi visitati
    queue = deque([(root, 0)])  # Coda per la BFS, con il nodo radice e il livello 0
    amplitude = 0  # Amplitude dell'albero

    while queue:
        node, level = queue.popleft()  # Estrae un nodo dalla coda
        if node not in visited:
            visited.add(node)
            amplitude = max(amplitude, level)  # Aggiorna l'ampiezza se necessario

            neighbors = graph.neighbors(node)  # Ottiene i vicini del nodo
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))  # Aggiunge i vicini alla coda con il livello incrementato

    return amplitude


def biu(graph):  # implementa metodo Bi(u), ritrona il nodo di eccentricità max nella fringe
    my_node = None
    max_ecc = -1
    ecc, fringe = bfs_livelli(graph)  # la fringe si ottiene invocando il nodo con massimo grado
    for node in fringe:
        e = eccentricity(graph, node)  # eccentricity viene calcolata facendo una bfs
        if e > max_ecc:
            max_ecc = e
            my_node = node
    return my_node, max_ecc
