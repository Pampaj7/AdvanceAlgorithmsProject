def find_author_with_most_collaborations(graph):
    max_collaborations = 0
    author_with_most_collaborations = None

    for node in graph.nodes:
        if node.startswith("Author:"):
            collaborations = len(set(graph.neighbors(node)))
            print(graph.neighbors(node))
            # la set serve a rimuovere i duplicati e quindi una volta cambiato di nodo serve a non ripetere sè stesso
            if collaborations > max_collaborations:
                max_collaborations = collaborations
                author_with_most_collaborations = node

    return author_with_most_collaborations, max_collaborations
