import networkx as nx
import tqdm as tqdm


def adapter_for_bipartiteGraphs(dataset_file):
    if dataset_file.find("out-dblp_article.csv") != -1:
        venue = 'journal'
    elif dataset_file.find("out-dblp_book.csv") != -1:
        venue = 'booktitle'
    elif dataset_file.find("out-dblp_incollection.csv") != -1:
        venue = 'booktitle'
    elif dataset_file.find("out-dblp_inproceedings.csv") != -1:
        venue = 'booktitle'
    elif dataset_file.find("out-dblp_mastersthesis.csv") != -1:
        venue = 'school'
    elif dataset_file.find("out-dblp_phdthesis.csv") != -1:
        venue = 'school'
    elif dataset_file.find("out-dblp_proceedings.csv") != -1:
        venue = 'title'
    elif dataset_file.find("DataSetTypeSmaller.csv") != -1:
        venue = 'journal'
    else:
        return 'journal'
    return venue


def build_bipartite_graph(dataset, dataset_file, mDate=2023):  # per 3 anni cambia parecchio
    G = nx.Graph()
    """
    author_dict = {}
    publication_dict = {}
    reverse_author_dict = {}
    reverse_publication_dict = {}
    venue_dict = {}
    """

    # function for creating the dictionary and his inverse
    """def creating_dictionary(node_dict, reverse_dict, node):
        if node not in node_dict:
            node_num = len(node_dict) + 1
            node_dict[node] = node_num
            reverse_dict[node_num] = node  # quite ez
    """
    # Create nodes for authors and publications
    for index, row in tqdm.tqdm(dataset.iterrows(), total=len(dataset), desc="Building bipartite graph"):

        authors = row['author']
        paper_date = row['mdate']  # year-month-day
        # date is a list with at place 0 year
        year_of_pub = paper_date.split('-')[0].strip()  # anno di mdate
        # strip elimina gli spazi dalla stringa

        venue = adapter_for_bipartiteGraphs(dataset_file)

        if isinstance(authors, str) and int(year_of_pub) <= mDate:
            """
            venue_dict[row[venue]] = {
                'year': row['year'],
                # 'title': row['title'],
                # 'pages': row['pages'],
                # 'publisher': row['publisher'],
                'venue': row[venue]
            } """
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

            G.nodes[publication_node]['label'] = {  # idem qui con tutte le info
                'type': 'publication',
                'id': publication_id,
                'year': row['year'],
                'year_of_pub': year_of_pub,
                'venue': row[venue]
            }
        """
        creating_dictionary(author_dict, reverse_author_dict, author_node)
        creating_dictionary(
            publication_dict, reverse_publication_dict, publication_node)
        """

    """
    G.graph['author_dict'] = author_dict
    G.graph['publication_dict'] = publication_dict
    G.graph['reverse_author_dict'] = reverse_author_dict
    G.graph['reverse_publication_dict'] = reverse_publication_dict
    """
    return G
