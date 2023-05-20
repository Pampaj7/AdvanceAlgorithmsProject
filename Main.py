from matplotlib import pyplot as plt

import BuildBipartiteGraph as bbg
import ExeptionCatcherCsv as ecc
import networkx as nx
import Find_oldest_venue as fov
import LowerBound as lw
import Diameter as d

dataset_file = 'Dataset/DataSetTypeSmaller.csv'

# exception handler for reading file
dataset = ecc.read_csv_ignore_errors(dataset_file)

# Build bipartite graph
bipartite_graph = bbg.build_bipartite_graph(dataset)

print(" Author Nodes:")
print('\n'.join(node for node in bipartite_graph.nodes() if node.startswith("Author:")), end="\n-----\n")
print("Publication Nodes:")
print('\n'.join(node for node in bipartite_graph.nodes() if node.startswith("Publication:")), end="\n-----\n")

# Print edges
print("Edges:")
for author, publication in bipartite_graph.edges():
    print(f"{author} --> {publication}")

# Print author dictionary
print("\nAuthor Dictionary:")
for author_node, author_num in bipartite_graph.graph['author_dict'].items():
    print(f"{author_node}: {author_num}")

# Print publication dictionary
print("\nPublication Dictionary:")
for publication_node, publication_num in bipartite_graph.graph['publication_dict'].items():
    print(f"{publication_node}: {publication_num}")

# Print reverse author dictionary
print("\nReverse Author Dictionary:")
for author_num, author_node in bipartite_graph.graph['reverse_author_dict'].items():
    print(f"{author_num}: {author_node}")

# Print reverse publication dictionary
print("\nReverse Publication Dictionary:")
for publication_num, publication_node in bipartite_graph.graph['reverse_publication_dict'].items():
    print(f"{publication_num}: {publication_node}")

pos = nx.random_layout(bipartite_graph)

node_color = ['blue' if 'Author:' in node else 'red' for node in bipartite_graph.nodes()]
edge_color = 'gray'
node_size = 50
edge_alpha = 0.5

plt.figure(figsize=(10, 8))

nx.draw(bipartite_graph, pos=pos, with_labels=False, node_color=node_color, edge_color=edge_color, node_size=node_size,
        alpha=edge_alpha)
plt.show()

# *---------------------------------------* end bipGraph construction and print


# *---------------------------------------* 1 --> First question
oldest_venue = fov.find_oldest_venue(bipartite_graph)
print("The oldest venue is:", oldest_venue)

# *---------------------------------------* 1 --> end question


# *---------------------------------------* 2 --> Diameter question

#altezza, last_node = lw.lower_Bound(bipartite_graph)
#print(altezza, last_node)

#cazz = d.calcola_diametro_grafo(bipartite_graph)
#print(cazz)

