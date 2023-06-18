def find_author_with_most_collaborations(
        graph):  # anche se vincent ha collaborato con 1488 articoli questo non significa che debba venire fuoori
    # questo numero, perchè se ha collaborato in un articolo diverso con lo stesso autore noi lo contiamo due volte
    max_collaborations = 0
    author_with_max_collaborations = None

    for node in graph.nodes:
        if 'label' in graph.nodes[node] and graph.nodes[node]['label']['type'] == 'author':
            if graph.nodes[node]['label']['name'] == 'Yang Liu 0099':
                print('ciao')
                print(graph.nodes[node]['label']['name'])
            collaborations = 0
            counted_authors = set()  # Set per tenere traccia degli autori già contati

            for neighbor in graph.neighbors(node):
                if 'label' in graph.nodes[neighbor] and graph.nodes[neighbor]['label']['type'] == 'publication':
                    authors = graph.neighbors(neighbor)

                    for author in authors:
                        if author != node and author not in counted_authors:
                            counted_authors.add(author)
                            collaborations += 1
            if graph.nodes[node]['label']['name'] == 'Yang Liu 0099':
                print('collab of ',' yang liu 0099: ',collaborations)
            if graph.nodes[node]['label']['name'] == 'Yang Liu':
                print('collab of ', ' yang liu: ', collaborations)
            if collaborations > max_collaborations:
                max_collaborations = collaborations
                author_with_max_collaborations = graph.nodes[node]['label']['name']

    return author_with_max_collaborations, max_collaborations
