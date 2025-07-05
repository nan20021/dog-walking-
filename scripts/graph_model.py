import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned & normalized edges
df = pd.read_csv('data/edges_normalized.csv')

# User preference weights
alpha, beta, gamma = 0.5, 0.3, 0.2

# Build graph with composite cost
G = nx.DiGraph()
for _, row in df.iterrows():
    cost = alpha * row['risk'] + beta * (1 - row['scenic']) + gamma * row['weather']
    G.add_edge(row['u'], row['v'], cost=cost)

# Example route
src, dst = 'A', 'C'  # replace with real node IDs
route = nx.shortest_path(G, src, dst, weight='cost')
total = sum(G[u][v]['cost'] for u, v in zip(route, route[1:]))
print(f"Route: {route}, total cost: {total:.3f}")

# Save visualization
pos = nx.spring_layout(G)
plt.figure(figsize=(8,6))
nx.draw(G, pos, node_size=10, edge_color='lightgray')
nx.draw_networkx_nodes(G, pos, nodelist=route, node_color='red', node_size=50)
nx.draw_networkx_edges(G, pos, edgelist=list(zip(route,route[1:])), edge_color='red', width=2)
plt.title('Example Optimal Dog-Walking Route')
plt.axis('off')
plt.tight_layout()
plt.savefig('docs/assets/route_example.png', dpi=150)

python scripts/graph_model.py
