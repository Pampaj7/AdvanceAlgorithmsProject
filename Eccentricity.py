import networkx as nx


def eccentricity(graph): # questo usa il textbook delle slide, non buono
    eccentricities = {}
    for node in graph.nodes:
        distances = nx.single_source_dijkstra_path_length(graph, node)
        max_distance = max(distances.values())
        eccentricities[node] = max_distance
    return max(eccentricities)
