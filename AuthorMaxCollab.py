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

