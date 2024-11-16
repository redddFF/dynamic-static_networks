import networkx as nx
import matplotlib.pyplot as plt

# Create a tree network
G = nx.balanced_tree(r=2, h=3)

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightcoral', edge_color='gray')
plt.title("Tree Network")
plt.show()
