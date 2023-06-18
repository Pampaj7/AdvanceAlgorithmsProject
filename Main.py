import BuildBipartiteGraph as bbg
import networkx as nx
import AuthorMaxCollab as amc
import ExeptionCatcherCsv as ecc
import AuthorGraph as ag
import Find_oldest_venue as fov
import FindSubGraphMax as fsgm
import Diameter as d
import time

import checkCollabs

import checkCollabs as cc

# *---------------------------------------* 1 --> end question


# *---------------------------------------* 2 --> Diameter question


# UNION GRAPH


dataset_files = [ r"/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_article.csv",
                  r"/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_book.csv",
                  r"/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_incollection.csv",
                  r"/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_inproceedings.csv",
                  r"/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_mastersthesis.csv",
                  r"/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_phdthesis.csv",
                  r"/Users/gianlucagiuliani/Desktop/dblp-all-csv/out-dblp_proceedings.csv"
                 ]
graph_list = []

for dataset in dataset_files:
    datasetClean = ecc.read_csv_ignore_errors(dataset)
    bipGraph = bbg.build_bipartite_graph(datasetClean, dataset)
    print("The oldest venue is: ", fov.find_oldest_venue(bipGraph))  # 1

    author, numCollab = amc.find_author_with_most_collaborations(bipGraph)  # 3
    print("Max collaboration author is: ",
          author, "With collaborations: ", numCollab)
    #print('verifico correttezza risultato della collab:')
    #print(cc.check_collab())
    graph_list.append(bipGraph)
    #print('generating node with max degree: ')
    #max_degree_node = d.findMaxDegreeNodeGraph(bipGraph)
    print('getting biu of max degree node: ')
    max_ecc_node, max_ecc = d.biu(bipGraph)
    start = time.time()


    # print(_)
    print("--- %s seconds ---" % (time.time() - start))
    #print(len(fringe))

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
print('Creating union graph..')
union_graph = nx.compose_all(graph_list)
oldest_venue = fov.find_oldest_venue(union_graph)
print("The oldest venue of the union graph is:", oldest_venue)


author, numCollab = amc.find_author_with_most_collaborations(union_graph)
print("Max collaboration author in union graph is: ",
      author, "With collaborations: ", numCollab)
print('diameter of union...')
start = time.time()
node, max_ecc = d.biu(union_graph)
print("--- %s seconds ---" % (time.time() - start))

#author_graph = ag.build_author_graph(union_graph)



