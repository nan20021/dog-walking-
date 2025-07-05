---
title: Methods & Implementation
---



This page explains how we prepare data, build our graph model, and compute optimal routes.

---


We use two primary raw sources:

1. **OpenStreetMap edges** (`data/raw_osm_edges.csv`)  
2. **Weather observations** (`data/raw_weather.csv`)  

Run the preprocessing script to merge, clean, normalize, and export:

```bash
python scripts/preprocess_edges.py


import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/edges_normalized.csv')


for col in ['risk','scenic','weather']:
    df[f'n_{col}'] = df[col] / df[col].max()


alpha, beta, gamma = 0.5, 0.3, 0.2


G = nx.DiGraph()
for _, row in df.iterrows():
    cost = (
        alpha * row['n_risk'] +
        beta  * (1 - row['n_scenic']) +
        gamma * row['n_weather']
    )
    G.add_edge(row['u'], row['v'], cost=cost)


src, dst = 'A', 'C'           # replace with real node IDs
route = nx.shortest_path(G, src, dst, weight='cost')
print("Route:", route)
print("Total cost:", sum(G[u][v]['cost'] for u,v in zip(route, route[1:])))


pos = nx.spring_layout(G)
plt.figure(figsize=(8,6))
nx.draw(G, pos, node_size=10, edge_color='lightgray')
nx.draw_networkx_nodes(G, pos, nodelist=route, node_color='red', node_size=50)
nx.draw_networkx_edges(G, pos, edgelist=list(zip(route,route[1:])), edge_color='red', width=2)
plt.title('Example Optimal Dog-Walking Route')
plt.axis('off')
plt.savefig('assets/route_example.png', dpi=150)

