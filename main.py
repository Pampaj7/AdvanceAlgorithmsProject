import pandas as pd
import networkx as nx

# Leggi il file CSV del dataset utilizzando Pandas
dataset_path = "/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_article.csv"
data = pd.read_csv(dataset_path)

# Crea un grafo bipartito vuoto
graph = nx.Graph()

# Dizionari per mappare gli identificatori dei nodi con gli autori e le pubblicazioni
author_dict = {}
publication_dict = {}
reverse_author_dict = {}
reverse_publication_dict = {}

# Aggiungi i nodi autore al grafo
author_id = 0
for index, row in data.iterrows():
    authors = row["authors"].split("|")
    publication_id = row["publication_id"]

    # Aggiungi gli autori al grafo e crea le corrispondenze tra autore e nodo
    for author in authors:
        if author not in author_dict:
            author_dict[author] = author_id  # for each author we got the index
            reverse_author_dict[author_id] = author  # building reverse dict (idk why)
            graph.add_node(author_id, bipartite=0)
            author_id += 1

    # Aggiungi la pubblicazione al grafo e crea la corrispondenza tra pubblicazione e nodo
    if publication_id not in publication_dict:
        publication_dict[publication_id] = author_id
        reverse_publication_dict[author_id] = publication_id
        graph.add_node(author_id, bipartite=1)
        author_id += 1

# Aggiungi gli archi tra autori e pubblicazioni
for index, row in data.iterrows():
    authors = row["authors"].split("|")
    publication_id = row["publication_id"]

    # Crea un arco tra ogni autore e la pubblicazione corrispondente
    for author in authors:
        author_node = author_dict[author]
        publication_node = publication_dict[publication_id]
        graph.add_edge(author_node, publication_node)

# Esempio di accesso ai nodi e archi del grafo
print("Numero di nodi: ", graph.number_of_nodes())
print("Numero di archi: ", graph.number_of_edges())

# Esempio di accesso alle informazioni sulla pubblicazione utilizzando il dizionario inverso
publication_node = publication_dict["8845787"]
publication_info = reverse_publication_dict[publication_node]
print("Informazioni sulla pubblicazione:", publication_info)

# Esempio di accesso agli autori di una pubblicazione
authors_of_publication = [reverse_author_dict[node] for node in graph.neighbors(publication_node) if
                          graph.nodes[node]["bipartite"] == 0]
print("Autori della pubblicazione:", authors_of_publication)
