import BuildBipartiteGraph as bbg
import networkx as nx
import AuthorMaxCollab as amc
import ExeptionCatcherCsv as ecc
import AuthorGraph as ag
import Find_oldest_venue as fov
import Diameter as d
import time

# import checkCollabs as cc

# *---------------------------------------* 1 --> end question


# *---------------------------------------* 2 --> Diameter question


# UNION GRAPH


dataset_files = [r"C:\Users\leona\OneDrive\Desktop\DataSets\out-dblp_article.csv",
                 r"C:\Users\leona\OneDrive\Desktop\DataSets\out-dblp_book.csv",
                 r"C:\Users\leona\OneDrive\Desktop\DataSets\out-dblp_incollection.csv",
                 r"C:\Users\leona\OneDrive\Desktop\DataSets\out-dblp_inproceedings.csv",
                 r"C:\Users\leona\OneDrive\Desktop\DataSets\out-dblp_mastersthesis.csv",
                 r"C:\Users\leona\OneDrive\Desktop\DataSets\out-dblp_phdthesis.csv",
                 r"C:\Users\leona\OneDrive\Desktop\DataSets\out-dblp_proceedings.csv"
                 ]
graph_list = []

for dataset in dataset_files:
    datasetClean = ecc.read_csv_ignore_errors(dataset)
    bipGraph = bbg.build_bipartite_graph(datasetClean, dataset)
    print("The oldest venue is: ", fov.find_oldest_venue(bipGraph))  # 1

    author, numCollab = amc.find_author_with_most_collaborations(bipGraph)  # 3
    print("Max collaboration author is: ",
          author, "With collaborations: ", numCollab)
    # print('verifico correttezza risultato della collab:')
    # print(cc.check_collab())
    graph_list.append(bipGraph)
    print('getting biu of max degree node: ')
    max_ecc_node, max_ecc = d.biu(bipGraph)
    start = time.time()
    print("--- %s seconds ---" % (time.time() - start))
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
node, max_ecc = d.biu(union_graph)
print("--- %s seconds ---" % (time.time() - start))

author_graph = ag.build_author_graph(union_graph)
