from collections import deque
import FindSubGraphMax as fsgm
import tqdm


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

    print('numero nodi fringe: ', len(last_level.keys()))
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


def biu(graph1):  # implementa metodo Bi(u), ritrona il nodo di eccentricità max nella fringe
    graph = fsgm.find_largest_connected_component(graph1)  # TODO move me to ifub
    my_node = None
    max_ecc = -1
    ecc, fringe = bfs_livelli(graph)  # la fringe si ottiene invocando il nodo con massimo grado

    progress_bar = tqdm.tqdm(total=len(fringe), desc="Processing nodes")

    for node in fringe:
        e = eccentricity(graph, node)  # eccentricity viene calcolata facendo una bfs
        if e > max_ecc:
            max_ecc = e
            my_node = node

        progress_bar.update(1)

    progress_bar.close()

    return my_node, max_ecc
