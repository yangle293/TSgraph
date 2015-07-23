import networkx as nx
import KeggPathway
import matplotlib.pyplot as plt
from parse_KGML import KGML2Graph

graphfile = 'hsa04115.xml'
graph = KGML2Graph(graphfile)[1]
genes_graph = graph.get_genes()
#print genes_graph.node['56']

#for (node1, node2) in genes_graph.edges(): print genes_graph.node[node1]['label'], genes_graph.node[node2]['label']

print genes_graph.node['56']['label']

pos =nx.spring_layout(genes_graph);
A = {}

for key in genes_graph.nodes(): A[key] = genes_graph.node[key]['label'].split(',')[0]

print A.values()
nx.draw_networkx_nodes(genes_graph,pos)
nx.draw_networkx_edges(genes_graph,pos)
nx.draw_networkx_labels(genes_graph,pos,labels = A)
plt.show()
