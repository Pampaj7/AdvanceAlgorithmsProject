import networkx as nx
import pandas as pd
import csv
import math

def create_bipartite_graph(dataset):
    G = nx.Graph()

    # Dizionari per associare gli ID dei nodi ai corrispondenti autori o pubblicazioni
    author_dict = {}
    publication_dict = {}
    reverse_author_dict = {}
    reverse_publication_dict = {}

    # Aggiungi i nodi degli autori e delle pubblicazioni al grafo
    for index, row in dataset.iterrows():
        authors = row['author']
        if isinstance(authors, str):
            authors = authors.split('|')
            publication_id = row['id']
        elif isinstance(authors, float) and math.isnan(authors):
            continue
        
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
            label = f"Year: {row['year']}, Title: {row['title']}, Pages: {row['pages']}, Publisher: {row['publisher']}"
            if 'journal' in dataset.columns:
                label += f", Venue: {row['journal']}"
            elif 'booktitle' in dataset.columns:
                label += f", Venue: {row['booktitle']}"
            G.nodes[publication_dict[publication_id]]['label'] = label
            
    # Aggiungi i dizionari di mapping come attributi del grafo
    G.graph['author_dict'] = author_dict
    G.graph['publication_dict'] = publication_dict
    G.graph['reverse_author_dict'] = reverse_author_dict
    G.graph['reverse_publication_dict'] = reverse_publication_dict

    return G

# Carica i dataset
out_dblp_article = pd.read_csv('/Users/pampaj/PycharmProjects/AdvanceAlgorithmsProject/Dataset/DataSetTypeSmaller.csv', skiprows=[13, 32], sep=';') # e che ne so del perchè non vanno ste righe
#out_dblp_incollection = pd.read_csv('/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_incollection.csv')
#out_dblp_inproceedings = pd.read_csv('out-dblp_inproceedings.csv')
#out_dblp_proceedings = pd.read_csv('out-dblp_proceedings.csv')

# Crea i grafi bipartiti
bipartite_graph_article = create_bipartite_graph(out_dblp_article)
#bipartite_graph_incollection = create_bipartite_graph(out_dblp_incollection)
#bipartite_graph_inproceedings = create_bipartite_graph(out_dblp_inproceedings)
#bipartite_graph_proceedings = create_bipartite_graph(out_dblp_proceedings)

print("Nodi autore:")
for author_id, author_name in bipartite_graph_article.graph['author_dict'].items():
    print(f"ID: {author_id}, Autore: {author_name}")

print("Nodi pubblicazione:")
for publication_id, publication_name in bipartite_graph_article.graph['publication_dict'].items():
    print(f"ID: {publication_id}, Pubblicazione: {publication_name}")



