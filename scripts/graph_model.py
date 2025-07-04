import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data/edges_normalized.csv')


for col in ['risk', 'scenic', 'weather']:
    data[f'norm_{col}'] = data[col] / data[col].max()


alpha, beta, gamma = 0.5, 0.3, 0.2 


G = nx.DiGraph()
for _, row in data.iterrows():
    cost = (
        alpha * row['norm_risk'] +
        beta * (1 - row['norm_scenic']) +
        gamma * row['norm_weather']
    )
    G.add_edge(
        row['u'], row['v'],
        length=row['length'],
        risk=row['norm_risk'],
        scenic=row['norm_scenic'],
        weather=row['norm_weather'],
        cost=cost
    )


source_node, target_node = 'A', 'C' 
route = nx.shortest_path(G, source_node, target_node, weight='cost')
cost_sum = sum(G[u][v]['cost'] for u, v in zip(route, route[1:]))
print(f"Optimal route from {source_node} to {target_node}: {route}")
print(f"Total cost: {cost_sum:.3f}")


pos = nx.spring_layout(G)
plt.figure(figsize=(8,6))
nx.draw(G, pos, node_size=10, edge_color='lightgray')
nx.draw_networkx_nodes(G, pos, nodelist=route, node_color='red', node_size=50)
nx.draw_networkx_edges(G, pos, edgelist=list(zip(route, route[1:])), edge_color='red', width=2)
plt.title('Optimal Dog-Walking Route')
plt.axis('off')
plt.savefig('assets/route_example.png', dpi=150)
