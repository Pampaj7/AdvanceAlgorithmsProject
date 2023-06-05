def find_oldest_venue(graph):
    oldest_year = str('inf')  # Initialize with a high value
    oldest_venue = None

    for node in graph.nodes:  # non segue nessun algoritmo, usa uno stack dove legge i nodi inseriti progressivamente
        if 'label' in graph.nodes[node] and graph.nodes[node]['label']['type'] == 'publication':
            year = str(graph.nodes[node]['label']['year'])
            venue = str(graph.nodes[node]['label']['venue'])

            if year < oldest_year and venue != 'nan':
                oldest_year = year
                oldest_venue = graph.nodes[node]['label']['venue']

    return oldest_venue
