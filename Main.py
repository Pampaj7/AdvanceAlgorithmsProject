from matplotlib import pyplot as plt

import BuildBipartiteGraph as bbg
import ExeptionCatcherCsv as nodeWithMaxEcc
import networkx as nx
import Find_oldest_venue as fov
import Diameter as d
import AuthorMaxCollab as amc
import scipy as sp
import FindSubGraphMax as fsgm
import Eccentricity as e
import ExeptionCatcherCsv as ecc

# TODO sistemare la ricerca per data, adesso è fatto il caricamento solo per data, da fixare
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
"""

dataset_files = ['/home/leonardo/Scrivania/datasets/out-dblp_article.csv',
                 '/home/leonardo/Scrivania/datasets/out-dblp_book.csv',
                 '/home/leonardo/Scrivania/datasets/out-dblp_incollection.csv',
                 '/home/leonardo/Scrivania/datasets/out-dblp_inproceedings.csv',
                 '/home/leonardo/Scrivania/datasets/out-dblp_mastersthesis.csv',
                 '/home/leonardo/Scrivania/datasets/out-dblp_phdthesis.csv',
                 '/home/leonardo/Scrivania/datasets/out-dblp_proceedings.csv']
graph_list = []

for dataset in dataset_files:
    datasetClean = ecc.read_csv_ignore_errors(dataset)
    bipGraph = bbg.build_bipartite_graph(datasetClean, dataset)
    graph_list.append(bipGraph)

union_graph = nx.compose_all(graph_list)
total_nodes = union_graph.number_of_nodes()
print(f"Total nodes in the union graph: {total_nodes}")
"""
