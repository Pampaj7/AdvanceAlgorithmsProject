import BuildBipartiteGraph as bbg
import networkx as nx
import AuthorMaxCollab as amc
import ExeptionCatcherCsv as ecc
import AuthorGraph as ag
import Find_oldest_venue as fov
import  FindSubGraphMax as fsgm

"""
dataset_file = r'/Users/pampaj/PycharmProjects/AdvanceAlgorithmsProject/Dataset/DATA100K.csv'

# exception handler for reading file
dataset = nodeWithMaxEcc.read_csv_ignore_errors(dataset_file)

# Build bipartite graph
bipartite_graph = bbg.build_bipartite_graph(dataset, dataset_file)


# *---------------------------------------* end bipGraph construction and print


# *---------------------------------------* 1 --> First question

oldest_venue = fov.find_oldest_venue(bipartite_graph)
print(" The oldest venue is:", oldest_venue)

# *---------------------------------------* 1 --> end question


# *---------------------------------------* 2 --> Diameter question
'''
maxSubGraph = fsgm.find_largest_connected_component(bipartite_graph)
print("trovato sottomax graph")
nodeDegree = d.findMaxDegreeNodeGraph(maxSubGraph)
nodeWithMaxEcc, maxfist = d.farthest_node_bfs(maxSubGraph, nodeDegree)
print("il sottografo massimo ha eccentricità massima: ", maxfist, "con nodo: ", nodeWithMaxEcc)
# print('eccentricità networkx: ', nx.eccentricity(maxSubGraph))
print("lista nodi a profondità: ", d.bfs_maxdepth(maxSubGraph, maxfist, nodeWithMaxEcc))
print("la massima eccentricità della fringe è: ", d.Biu(maxSubGraph, maxfist, nodeWithMaxEcc))
# TODO da trovare implementazione per bene
# TODO il problema è nel calcolo dell'eccentricità
# TODO e dentro il codice dobbiamo troavre come implementare lo shortest path
'''

# *---------------------------------------* 2 --> end question


# *---------------------------------------* 3 --> Author max collab

author, numCollab = amc.find_author_with_most_collaborations(bipartite_graph)
print("L'autore con massimo numero di collaborazioni è: ",
      author, "con numero di collaborazioni: ", numCollab)

# print("vincent ha collaborato in : ",
#     amc.count_publications_of_author(bipartite_graph, "Author:H. Vincent Poor"))

# *---------------------------------------* 3 --> End Author max collab
"""

# UNION GRAPH


dataset_files = [  # '/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_article.csv',
    '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_book.csv',
    '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_incollection.csv',
    # '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_inproceedings.csv',  # grosso
    # '/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_mastersthesis.csv',
    # '/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_phdthesis.csv',
    # '/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_proceedings.csv'
]
graph_list = []

for dataset in dataset_files:
    datasetClean = ecc.read_csv_ignore_errors(dataset)
    bipGraph = bbg.build_bipartite_graph(datasetClean, dataset)
    print("\nThe oldest venue is: ", fov.find_oldest_venue(bipGraph))  # 1
    # diam
    author, numCollab = amc.find_author_with_most_collaborations(bipGraph)  # 3
    print("Max collaboration author is: ",
          author, "With collaborations: ", numCollab)

    graph_list.append(bipGraph)

print('Creating union graph..')
union_graph = nx.compose_all(graph_list)

oldest_venue = fov.find_oldest_venue(union_graph)
print("The oldest venue of the union graph is:", oldest_venue)

author, numCollab = amc.find_author_with_most_collaborations(union_graph)
print("Max collaboration author in union graph is: ",
      author, "With collaborations: ", numCollab)

print('Creating author graph..')
author_graph = ag.build_author_graph(union_graph)
