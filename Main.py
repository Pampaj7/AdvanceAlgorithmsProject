import BuildBipartiteGraph as bbg
import networkx as nx
import AuthorMaxCollab as amc
import ExeptionCatcherCsv as ecc
import AuthorGraph as ag
import Find_oldest_venue as fov
import Diameter as d
import time

dataset_files = [r"dblp-all-csv/out-dblp_article.csv",
                 r"dblp-all-csv/out-dblp_book.csv",
                 #r"dblp-all-csv/out-dblp_incollection.csv",
                 #r"dblp-all-csv/out-dblp_inproceedings.csv",
                 #r"dblp-all-csv/out-dblp_mastersthesis.csv",
                 #r"dblp-all-csv/out-dblp_phdthesis.csv",
                 #r"dblp-all-csv/out-dblp_proceedings.csv"
                 ]

graph_list = []

for dataset in dataset_files:
    datasetClean = ecc.read_csv_ignore_errors(dataset)
    bipGraph = bbg.build_bipartite_graph(datasetClean, dataset)


    strt = time.time()
    print("The oldest venue is: ", fov.find_oldest_venue(bipGraph))  # 1
    print("--- %s seconds ---" % (time.time() - strt))

    strt = time.time()

    author, numCollab = amc.find_author_with_most_collaborations(bipGraph)  # 3
    print("Max collaboration author is: ",
          author, "With collaborations: ", numCollab)
    print("--- %s seconds ---" % (time.time() - strt))

    strt = time.time()
    print("the diameter is: ", d.iFub(bipGraph))  # 2
    print("--- %s seconds ---" % (time.time() - strt))

    graph_list.append(bipGraph)
    del bipGraph  # dealloca ram

print('Creating union graph..')
union_graph = nx.compose_all(graph_list)
del graph_list

oldest_venue = fov.find_oldest_venue(union_graph)
print("The oldest venue of the union graph is:", oldest_venue)

author, numCollab = amc.find_author_with_most_collaborations(union_graph)
print("Max collaboration author in union graph is: ",
      author, "With collaborations: ", numCollab)

print('diameter of union...')

start = time.time()

print("The diameter is: ", d.iFub(union_graph))

print("--- %s seconds ---" % (time.time() - start))

author_graph = ag.build_author_graph(union_graph)
