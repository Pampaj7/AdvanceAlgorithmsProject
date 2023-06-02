from matplotlib import pyplot as plt

import BuildBipartiteGraph as bbg
import ExeptionCatcherCsv as ecc
import networkx as nx
import Find_oldest_venue as fov
import LowerBound as lw
import Diameter as d
import AuthorMaxCollab as amc

dataset_file = '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_article.csv'

# exception handler for reading file
#dataset = ecc.read_csv_ignore_errors(dataset_file)

# Build bipartite graph
bipartite_graph = bbg.build_bipartite_graph(ecc.read_csv_ignore_errors(dataset_file))

"""
print(" Author Nodes:")
print('\n'.join(node for node in bipartite_graph.nodes()
      if node.startswith("Author:")), end="\n-----\n")
print("Publication Nodes:")
print('\n'.join(node for node in bipartite_graph.nodes()
      if node.startswith("Publication:")), end="\n-----\n")

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
"""

# *---------------------------------------* end bipGraph construction and print


# *---------------------------------------* 1 --> First question

oldest_venue = fov.find_oldest_venue(bipartite_graph)
print(" The oldest venue is:", oldest_venue)

# *---------------------------------------* 1 --> end question


# *---------------------------------------* 2 --> Diameter question

# altezza, last_node = lw.lower_Bound(bipartite_graph)
# print(altezza, last_node)

# cazz = d.calcola_diametro_grafo(bipartite_graph)
# print(cazz)
print("Il diametro del grafo è: ", d.calcola_diametro_grafo(bipartite_graph))

# *---------------------------------------* 2 --> end question


# *---------------------------------------* 3 --> Author max collab

author, numCollab = amc.find_author_with_most_collaborations(bipartite_graph)
print("L'autore con massimo numero di collaborazioni è: ",
      author, "con numero di collaborazioni: ", numCollab)

# *---------------------------------------* 3 --> End Author max collab
