import networkx as nx
import pandas as pd
import csv

def create_bipartite_graph(dataset):
    G = nx.Graph()

    # Dizionari per associare gli ID dei nodi ai corrispondenti autori o pubblicazioni
    author_dict = {}
    publication_dict = {}
    reverse_author_dict = {}
    reverse_publication_dict = {}

    # Aggiungi i nodi degli autori e delle pubblicazioni al grafo
    for index, row in dataset.iterrows():
        authors = row['author'].split('|')
        publication_id = row['id']

        for author in authors:
            # Aggiungi l'autore come nodo nel grafo
            if author not in author_dict:
                author_dict[author] = len(author_dict)
                reverse_author_dict[len(reverse_author_dict)] = author

            # Aggiungi un arco tra l'autore e la pubblicazione
            G.add_edge(author_dict[author], publication_dict.get(publication_id, len(publication_dict)))

        # Aggiungi la pubblicazione come nodo nel grafo
        if publication_id not in publication_dict:
            publication_dict[publication_id] = len(publication_dict)
            reverse_publication_dict[len(reverse_publication_dict)] = publication_id
            G.nodes[publication_dict[publication_id]]['label'] = f"Year: {row['year']}, Title: {row['title']}, Pages: {row['pages']}, Publisher: {row['publisher']}, Venue: {row['journal'] if 'article' in dataset.name else row['booktitle']}"

    # Aggiungi i dizionari di mapping come attributi del grafo
    G.graph['author_dict'] = author_dict
    G.graph['publication_dict'] = publication_dict
    G.graph['reverse_author_dict'] = reverse_author_dict
    G.graph['reverse_publication_dict'] = reverse_publication_dict

    return G



# Carica i dataset
out_dblp_article = pd.read_csv('/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_article.csv', error_bad_lines=False)
#out_dblp_incollection = pd.read_csv('/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_incollection.csv')
#out_dblp_inproceedings = pd.read_csv('out-dblp_inproceedings.csv')
#out_dblp_proceedings = pd.read_csv('out-dblp_proceedings.csv')

# Crea i grafi bipartiti
bipartite_graph_article = create_bipartite_graph(out_dblp_article)
#bipartite_graph_incollection = create_bipartite_graph(out_dblp_incollection)
#bipartite_graph_inproceedings = create_bipartite_graph(out_dblp_inproceedings)
#bipartite_graph_proceedings = create_bipartite_graph(out_dblp_proceedings)


