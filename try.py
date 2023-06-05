import networkx as nx

# Crea due grafi di esempio
graph1 = nx.Graph()
graph1.add_edges_from([(1, 2), (2, 3), (3, 4)])

graph2 = nx.Graph()
graph2.add_edges_from([(1, 2), (1, 3), (5, 6)])

# Crea il grafo di unione
union_graph = nx.compose(graph1, graph2)

# Stampa i nodi e gli archi del grafo di unione
print("Nodi:", union_graph.nodes)
print("Archi:", union_graph.edges)

dataset_file = '/home/leonardo/Scrivania/datasets/out-dblp_book.csv'

print(dataset_file)
