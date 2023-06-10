import networkx as nx
from tqdm import tqdm


def build_author_graph(graph):
    max_edge = None
    max_collab = 0
    author_graph = nx.Graph()
    num_nodes = len(graph.nodes)
    progress_bar = tqdm(total=num_nodes, desc="Building author graph")

    for node in graph.nodes:
        progress_bar.update(1)

        if 'label' in graph.nodes[node] and graph.nodes[node]['label']['type'] == 'author':
            author_graph.add_node(node)  # il grafo ha tutti e solo i nodi autore

        for neighbour in graph.neighbors(node):
            if 'label' in graph.nodes[node] and graph.nodes[node]['label']['type'] == 'publication':
                authors = graph.neighbors(neighbour)

                for author in authors:
                    if author_graph.has_edge(author, node):
                        author_graph[node][author]['weight'] += 1
                        if author_graph[node][author]['weight'] > max_collab:
                            max_collab = author_graph[node][author]['weight']
                            max_edge = (node, author)
                    else:
                        author_graph.add_edge(node, author, weight=1)
    progress_bar.close()
    print('collaborazione più forte: ', max_edge, ' con num collab: ', max_collab)

    return None
