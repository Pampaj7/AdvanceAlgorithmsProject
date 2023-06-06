import networkx as nx


def find_author_with_most_collaborations(graph):
    max_collaborations = 0
    author_with_max_collaborations = None

    for node in graph.nodes:
        if 'label' in graph.nodes[node] and graph.nodes[node]['label']['type'] == 'author':
            collaborations = 0
            counted_authors = set()  # Set per tenere traccia degli autori già contati

            for neighbor in graph.neighbors(node):
                if 'label' in graph.nodes[neighbor] and graph.nodes[neighbor]['label']['type'] == 'publication':
                    authors = graph.neighbors(neighbor)

                    for author in authors:
                        if author != node:
                            counted_authors.add(author)
                            collaborations += 1

            if collaborations > max_collaborations:
                max_collaborations = collaborations
                author_with_max_collaborations = graph.nodes[node]['label']['name']

    return author_with_max_collaborations, max_collaborations


def count_publications_of_author(graph, author_node):
    count = 0

    for neighbor in graph.neighbors(author_node):
        if 'label' in graph.nodes[neighbor] and graph.nodes[neighbor]['label']['type'] == 'publication':
            count += 1

    return count

"""
# Creazione del grafo
graph = nx.Graph()

# Aggiunta dei nodi autore
graph.add_node("Author1", label={'type': 'author', 'name': 'Author 1'})
graph.add_node("Author2", label={'type': 'author', 'name': 'Author 2'})
graph.add_node("Author3", label={'type': 'author', 'name': 'Author 3'})

# Aggiunta dei nodi collaborazione
graph.add_node("Collab1", label={'type': 'publication', 'id': 1})
graph.add_node("Collab2", label={'type': 'publication', 'id': 2})
graph.add_node("Collab3", label={'type': 'publication', 'id': 3})
graph.add_node("Collab4", label={'type': 'publication', 'id': 4})
graph.add_node("Collab5", label={'type': 'publication', 'id': 5})


# Aggiunta degli archi tra autori e collaborazioni
graph.add_edge("Author1", "Collab1")
graph.add_edge("Author1", "Collab2")
graph.add_edge("Author2", "Collab1")
graph.add_edge("Author2", "Collab3")
graph.add_edge("Author3", "Collab2")
graph.add_edge("Author3", "Collab3")
graph.add_edge("Author1", "Collab3")
graph.add_edge("Author3", "Collab1")


print(find_author_with_most_collaborations(graph))

"""
