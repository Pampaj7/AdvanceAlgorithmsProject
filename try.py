import networkx as nx
import pandas as pd
import ProgressionBar as pb
import math


def build_bipartite_graph(dataset):
    G = nx.Graph()

    # Create nodes for authors and publications
    for index, row in dataset.iterrows():
        pb.print_progress_bar(index, len(dataset),
                              prefix='Progress:', suffix='Complete', length=50)
        authors = row['author']
        if isinstance(authors, str):
            authors = authors.split('|')
            publication_id = row['id']
        elif isinstance(authors, float) and math.isnan(authors):
            continue

        for author in authors:  # chat said that in networkx we don't neet to do the add, add_edge automatically adds
            # the node
            G.add_edge("Author:" + author,
                       "Publication:" + str(publication_id))

    return G


dataset_file = '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_article.csv'

# Load dataset
dataset = pd.read_csv(dataset_file, skiprows=[13, 32], sep=';')

# Build bipartite graph
bipartite_graph = build_bipartite_graph(dataset)

# Print nodes and edges for the bipartite graph
print("Author Nodes:")
print('\n'.join(node for node in bipartite_graph.nodes()
      if node.startswith("Author:")), end="\n-----\n")
print("Publication Nodes:")
print('\n'.join(node for node in bipartite_graph.nodes()
      if node.startswith("Publication:")), end="\n-----\n")

print("Edges:")
for edge in bipartite_graph.edges():
    print(edge)
