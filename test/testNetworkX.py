import matplotlib.pyplot as plt
import networkx as nx

G = nx.fast_gnp_random_graph(10,0.2)

nx.draw_circular(G)
plt.show()