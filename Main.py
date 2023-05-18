import BuildBipartiteGraph as bbg
import ExeptionCatcherCsv as ecc

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
