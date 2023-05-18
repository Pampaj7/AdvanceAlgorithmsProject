import networkx as nx
import pandas as pd
import math
import ProgressionBar as pb


# TODO node of the BIgraph with Source Author and Destination is a Publication
# TODO componente connessa
# TODO diametro
def create_bipartite_graph(dataset):
    G = nx.Graph()

    author_dict = {}
    publication_dict = {}
    reverse_author_dict = {}
    reverse_publication_dict = {}

    def add_author(author):
        if author not in author_dict:
            author_dict[author] = len(author_dict)
            reverse_author_dict[len(reverse_author_dict)] = author

    def create_node():
        for row in dataset:
            authors = dataset.iloc[row]['author']
            authors = authors.split('|')


    def add_publication(publication_id, row):
        if publication_id not in publication_dict:
            publication_dict[publication_id] = len(publication_dict)
            label = f"Year: {row['year']}, Title: {row['title']}, Pages: {row['pages']}, Publisher: {row['publisher']}"
            if 'journal' in dataset.columns:
                label += f", Venue: {row['journal']}"
            elif 'booktitle' in dataset.columns:
                label += f", Venue: {row['booktitle']}"
            G.add_node(publication_dict[publication_id], label=label)

    for index, row in dataset.iterrows():  # TODO porta a lineare
        pb.print_progress_bar(index, len(dataset), prefix='Progress:', suffix='Complete', length=50)
        authors = row['author']
        if isinstance(authors, str):
            authors = authors.split('|')
            publication_id = row['id']
        elif isinstance(authors, float) and math.isnan(authors):
            continue

        for author in authors:  # TODO find better way
            add_author(author)
            G.add_edge(author_dict[author], publication_dict.get(publication_id, len(publication_dict)))

        add_publication(publication_id, row)

    G.graph['author_dict'] = author_dict  # TODO each node must be an author and a publication
    G.graph['publication_dict'] = publication_dict
    G.graph['reverse_author_dict'] = reverse_author_dict
    G.graph['reverse_publication_dict'] = reverse_publication_dict

    return G


out_dblp_article = pd.read_csv('Dataset/DataSetTypeSmaller.csv',
                               skiprows=[13, 32], sep=';')

bipartite_graph_article = create_bipartite_graph(out_dblp_article)

print("Nodi autore:")
for author_id, author_name in bipartite_graph_article.graph['author_dict'].items():
    print(f"ID: {author_id}, Autore: {author_name}")

print("Nodi pubblicazione:")
for publication_id, publication_name in bipartite_graph_article.graph['publication_dict'].items():
    print(f"ID: {publication_id}, Pubblicazione: {publication_name}")
