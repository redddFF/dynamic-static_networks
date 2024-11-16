import networkx as nx
import matplotlib.pyplot as plt

# Create a ring network
G = nx.cycle_graph(6)

# Draw the graph
nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray')
plt.title("Ring Network")
plt.show()
