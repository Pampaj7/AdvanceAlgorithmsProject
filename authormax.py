# ricerco le collaborazioni massime degli autori
# esplorando i nodi pubblicazione.
import operator


def max_collab_from_publish(graph):
    my_authors = {}  # dict dove metto gli autori come key e come value le collaborazioni
    for node in graph.nodes:  # itero su tutti i nodi pubblicazione
        if 'label' in graph.nodes[node] and graph.nodes[node]['label']['type'] == 'publication':
            authors_of_publication = graph.neighbors(node)
            #lenght = len(authors_of_publication)
            for neighbor in authors_of_publication:  # cerco gli autori della pubblicazione
                if neighbor not in my_authors:  # inserisco i nuovi autori in un dizionario e inizializzo il value
                    my_authors[neighbor] = 0  # cioe il numero di collaborazioni a 0 in tal caso
                #my_authors[neighbor] += lenght

    x = max(my_authors.items(), key=operator.itemgetter(1))
    print(x)
    print(my_authors[x])
