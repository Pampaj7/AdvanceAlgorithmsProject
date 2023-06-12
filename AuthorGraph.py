import networkx as nx
from tqdm import tqdm


def build_author_graph(graph):
    max_edge = None
    max_collab = 0
    author_graph = nx.Graph()  # generazione nuovo grafo
    num_nodes = len(graph.nodes)  # per prograss bar
    progress_bar = tqdm(total=num_nodes, desc="Building author graph")

    for node in graph.nodes:  # gurado tutti i nodi dello union
        progress_bar.update(1)

        if 'label' in graph.nodes[node] and graph.nodes[node]['label']['type'] == 'author':  # se è un autore
            author_graph.add_node(node)  # il grafo ha tutti e solo i nodi autore

        for neighbour in graph.neighbors(node):#cerco i vicini del nodo, se sono publications
            if 'label' in graph.nodes[neighbour] and graph.nodes[neighbour]['label']['type'] == 'publication':
                authors = graph.neighbors(neighbour)#aggiungo i vicini del vicino, autori quindi, in authors

                for author in authors:
                    if author_graph.has_edge(author, node):#aumento il peso dell'arco già esistente
                        author_graph[node][author]['weight'] += 1
                        if author_graph[node][author]['weight'] > max_collab:
                            max_collab = author_graph[node][author]['weight']#aggiorno per trovare la collaborazione
                            max_edge = (node, author)#migliore e la cerico nell'arco max_edge
                            print('max edge ', max_edge)
                    elif graph.nodes[node] is not graph.nodes[author]:#se l'arco non esiste lo creo, con peso 1
                        author_graph.add_edge(node, author, weight=1)
    progress_bar.close()
    print('collaborazione più forte: ', max_edge, ' con num collab: ', max_collab)

    return None
