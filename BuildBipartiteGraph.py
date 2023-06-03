import networkx as nx
import ProgressionBar as pb


def build_bipartite_graph(dataset, mDate=2020):
    G = nx.Graph()

    author_dict = {}
    publication_dict = {}
    reverse_author_dict = {}
    reverse_publication_dict = {}
    venue_dict = {}

    # function for creating the dictionary and his inverse
    def creating_dictionary(node_dict, reverse_dict, node):
        if node not in node_dict:
            node_num = len(node_dict) + 1
            node_dict[node] = node_num
            reverse_dict[node_num] = node  # quite ez

    # Create nodes for authors and publications
    for index, row in dataset.iterrows():  # common iteration

        pb.print_progress_bar(index, len(dataset), prefix='Progress:', suffix='Complete', length=50)  # progress bar

        authors = row['author']
        paper_date = row['mdate']  # year-month-day
        # date is a list with at place 0 year
        year_of_pub = paper_date.split('-')[0].strip()
        # strip elimina gli spazi dalla stringa
        if isinstance(authors, str) and int(year_of_pub) <= mDate:
            if 'journal' in dataset.columns:
                venue_dict[row['journal']] = {
                    'year': row['year'],
                    'title': row['title'],
                    'pages': row['pages'],
                    'publisher': row['publisher'],
                    'venue': row['journal']
                }
            if 'journal' not in dataset.columns:  # book.csv non ha journal :0
                venue_dict[row['school']] = {
                    'year': row['year'],
                    'title': row['title'],
                    'pages': row['pages'],
                    'publisher': row['publisher'],
                    'venue': row['school']
                }
            authors = authors.split('|')
            publication_id = row['id']
        else:
            continue

        for author in authors:
            author_node = "Author:" + author
            publication_node = "Publication:" + str(publication_id)

            G.add_edge(author_node, publication_node)  # fa tutto qui

            G.nodes[author_node]['label'] = {  # per ogni autore adesso hanno una label con nome e tipo
                'type': 'author',
                'name': author
            }

            if 'journal' in dataset.columns:
                G.nodes[publication_node]['label'] = {  # idem qui con tutte le info
                    'type': 'publication',
                    'id': publication_id,
                    'year': row['year'],
                    'title': row['title'],
                    # se ci mettiamo un dizionario tipo colums si può associare vari nomi alla stessa struttura
                    'pages': row['pages'],
                    'publisher': row['publisher'],
                    'venue': row['journal']
                }

            if 'journal' not in dataset.columns:  # book.csv non ha journal :0
                G.nodes[publication_node]['label'] = {  # idem qui con tutte le info
                    'type': 'publication',
                    'id': publication_id,
                    'year': row['year'],
                    'title': row['title'],
                    # se ci mettiamo un dizionario tipo colums si può associare vari nomi alla stessa struttura
                    'pages': row['pages'],
                    'publisher': row['publisher'],
                    'venue': row['school']
                }

            creating_dictionary(author_dict, reverse_author_dict, author_node)
            creating_dictionary(
                publication_dict, reverse_publication_dict, publication_node)

    # Set dictionaries as graph attributes La riga G.graph['author_dict'] = author_dict imposta il dizionario
    # author_dict come attributo 'author_dict' del grafo G. Questo attributo può essere utilizzato per accedere al
    # dizionario dei nodi degli autori nel grafo. Questo è utile perché consente di memorizzare i dizionari come
    # parte del grafo stesso, in modo che siano accessibili insieme al grafo stesso. Ciò semplifica l'accesso e
    # l'utilizzo dei dizionari di mapping associati al grafo senza doverli gestire separatamente.

    #           |
    #           |
    #           |
    #           |
    #           V

    G.graph['author_dict'] = author_dict
    G.graph['publication_dict'] = publication_dict
    G.graph['reverse_author_dict'] = reverse_author_dict
    G.graph['reverse_publication_dict'] = reverse_publication_dict

    return G
