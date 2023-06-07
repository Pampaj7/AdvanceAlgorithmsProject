import networkx as nx


def find_largest_connected_component(graph):
    largest_component = None
    max_size = 0

    for component in nx.connected_components(graph):
        component_size = len(component)
        if component_size > max_size:
            largest_component = component
            max_size = component_size

    return graph.subgraph(largest_component)
