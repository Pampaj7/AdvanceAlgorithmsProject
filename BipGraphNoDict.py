import networkx as nx
import pandas as pd
import ProgressionBar as pb
import math


def build_bipartite_graph(dataset):
    G = nx.Graph()
    # Create nodes for authors and publications
    for index, row in dataset.iterrows():
        pb.print_progress_bar(index, len(dataset), prefix='Progress:', suffix='Complete', length=50)
        authors = row['author']
        if isinstance(authors, str):
            authors = authors.split('|')
            publication_id = row['id']
        elif isinstance(authors, float) and math.isnan(authors):
            continue

        for author in authors:
            G.add_edge(author, publication_id)

    return G

