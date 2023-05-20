import networkx as nx
import random
from collections import deque

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


def lower_Bound(G):
    source = random.choice(list(G.nodes))
    treeRX = nx.bfs_tree(G, source=source)
    distRX, x = calcola_altezza_Albero(treeRX)

    # Trova il nodo più distante da x nel sottografo rimanente
    treeXY = nx.bfs_tree(G.subgraph(treeRX.nodes - [x]), source=x)
    distXY, y = calcola_altezza_Albero(treeXY)
    print('distanza: '+distRX)
    print('ultimo elemento: '+x)
    lower_bound = distRX + distXY

    return lower_bound


def calcola_altezza_Albero(grafo):
    nodo_radice = random.choice(list(grafo.nodes))

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

    return altezza_massima, nodo_altezza_massima


# Esempio di utilizzo
grafo = nx.Graph()
grafo.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('B', 'C')])