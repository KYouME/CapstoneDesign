import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt

#무방향성 그래프
g1 = nx.Graph()
g1.add_nodes_from((1,2,3,4,5))
g1.add_edges_from([(1,2), (1,3),(1,4),(3,5)])

nx.draw(g1)

#방향성 가중치 그래프
g2 = nx.DiGraph() 

g2.add_weighted_edges_from([(1, 2, 3), (2, 3, 4)])
g2.add_edge(1, 3, weight = 6)

pos = nx.spring_layout(g2)
nx.draw(g2, pos = pos, with_labels = True)

labels = nx.get_edge_attributes(g2,'weight')
nx.draw_networkx_edge_labels(g2, pos, edge_labels = labels);


plt.show()