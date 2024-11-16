import networkx as nx
import matplotlib.pyplot as plt

# Create a hypercube network
G = nx.hypercube_graph(3)

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.title("Hypercube Network")
plt.show()
