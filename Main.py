import BuildBipartiteGraph as bbg
import networkx as nx
import AuthorMaxCollab as amc
import ExeptionCatcherCsv as ecc
import AuthorGraph as ag
import Find_oldest_venue as fov
import FindSubGraphMax as fsgm
import Diameter as d

# *---------------------------------------* 1 --> end question


# *---------------------------------------* 2 --> Diameter question


# UNION GRAPH


dataset_files = ['/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_article.csv',  # grosso
                 '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_book.csv',
                 '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_incollection.csv',
                 # '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_inproceedings.csv',  # grosso
                 '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_mastersthesis.csv',
                 '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_phdthesis.csv',
                 '/Users/pampaj/Desktop/DataSet/dblp-all-csv/out-dblp_proceedings.csv'
                 ]
graph_list = []

for dataset in dataset_files:
    datasetClean = ecc.read_csv_ignore_errors(dataset)
    bipGraph = bbg.build_bipartite_graph(datasetClean, dataset)
    print("The oldest venue is: ", fov.find_oldest_venue(bipGraph))  # 1

    author, numCollab = amc.find_author_with_most_collaborations(bipGraph)  # 3
    print("Max collaboration author is: ",
          author, "With collaborations: ", numCollab)

    # diam 2
"""
    maxSubGraph = fsgm.find_largest_connected_component(bipGraph)  # ok
    print("trovato sottomax graph")
    nodeDegree = d.findMaxDegreeNodeGraph(maxSubGraph)  # nodo + connesso

    nodeWithMaxEcc, maxfist = d.farthest_node_bfs(maxSubGraph, nodeDegree)
    print("il sottografo massimo ha eccentricità massima: ", maxfist, "con nodo: ", nodeWithMaxEcc)
    print("lista nodi a profondità: ", d.bfs_maxdepth(maxSubGraph, maxfist, nodeWithMaxEcc))
    print("la massima eccentricità della fringe è: ", d.Biu(maxSubGraph, maxfist, nodeWithMaxEcc))
"""

graph_list.append(bipGraph)

print('Creating union graph..')
union_graph = nx.compose_all(graph_list)

oldest_venue = fov.find_oldest_venue(union_graph)
print("The oldest venue of the union graph is:", oldest_venue)

author, numCollab = amc.find_author_with_most_collaborations(union_graph)
print("Max collaboration author in union graph is: ",
      author, "With collaborations: ", numCollab)

author_graph = ag.build_author_graph(union_graph)
