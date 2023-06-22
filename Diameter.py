from collections import deque
import FindSubGraphMax as fsgm
import tqdm


# ritorna il nodo di max grado per ottimizzare calcolo esatto del diametro
def findMaxDegreeNodeGraph(graph):
    max_deg = 0
    max_deg_node = None
    for node in graph.nodes():
        if max_deg < graph.degree(node):
            max_deg = graph.degree(node)
            max_deg_node = node
    return max_deg_node


def bfs_livelli(graph, start_node, i, year_of_pub=2023):  # ritrona la fringe, calcola da solo il nodo con massimo grado
    visited = set()
    last_level = {}

    queue = deque([(start_node, 0)])
    livelli = {start_node: 0}

    while queue:
        node, level = queue.popleft()
        if level == i and node not in last_level:
            # print('inserisco il nodo: ', node)
            if ('label' in graph.nodes[node] and graph.nodes[node]['label']['type'] == 'publication' and int(
                    graph.nodes[node]['label']['year_of_pub']) <= year_of_pub) or (
                    'label' in graph.nodes[node] and graph.nodes[node]['label']['type'] == 'author'):
                last_level[node] = 0
        if node not in visited:
            # print(node)
            visited.add(node)
            neighbors = graph.neighbors(node)

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))
                    livelli[neighbor] = level + 1

    print('Fringe number of nodes: ', len(last_level.keys()))
    return last_level.keys()


def eccentricity(graph, root):
    visited = set()
    queue = deque([(root, 0)])
    amplitude = 0

    while queue:
        node, level = queue.popleft()
        if node not in visited:
            visited.add(node)
            amplitude = max(amplitude, level)

            neighbors = graph.neighbors(node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))

    return amplitude


def biu(graph, start_node, i):  # implementa metodo Bi(u), ritrona il nodo di eccentricità max nella fringe
    max_ecc = -1
    fringe = bfs_livelli(graph, start_node, i)  # la fringe si ottiene invocando il nodo con massimo grado

    progress_bar = tqdm.tqdm(total=len(fringe), desc="Processing nodes")

    for node in fringe:
        e = eccentricity(graph, node)  # eccentricity viene calcolata facendo una bfs
        if e > max_ecc:
            max_ecc = e

        progress_bar.update(1)

    progress_bar.close()

    return max_ecc


def iFub(graph1):
    graph = fsgm.find_largest_connected_component(graph1)
    start_node = findMaxDegreeNodeGraph(graph)

    i = eccentricity(graph, start_node)
    lb = i
    ub = 2 * i
    while ub > lb:
        biuu = biu(graph, start_node, i)
        if max(lb, biuu) > 2 * (i - 1):
            return max(lb, biuu)
        else:
            lb = max(lb, biuu)
            ub = 2 * (i - 1)
        i = i - 1
    return lb
