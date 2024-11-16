import networkx as nx
import matplotlib.pyplot as plt

# Create a mesh network
G = nx.complete_graph(6)

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightgreen', edge_color='gray')
plt.title("Mesh Network")
plt.show()
