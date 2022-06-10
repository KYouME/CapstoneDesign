from pyvis.network import Network
import pandas as pd
import networkx as nx

net = Network(height='800', width='100%', bgcolor='#222222', font_color='white')

net.force_atlas_2based()
got_data_ratings = pd.read_csv('ratings_small.csv')
users = got_data_ratings['USER_KEY']
movies = got_data_ratings['MOVIE_KEY']
weights = got_data_ratings['rating']

edge_data = zip(users, movies, weights)

for d in edge_data:
    net.add_node(d[0],size=50,color='#00D8FF')
    net.add_node(d[1],size=25,color='#CEFBC9', shape='square')
    net.add_edge(d[0], d[1], color="white", label = str(d[2]), arrows='to')

#net.show_buttons(filter_=True)
net.show('ratings_small_graph.html')



