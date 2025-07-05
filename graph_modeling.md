---
title: Methods & Implementation
---



This page walks through our data preparation, graph modeling, pathfinding, and plotting pipeline for the Optimal Dog-Walking Route Recommendation System.

---


We combine two raw data sources:

- **OpenStreetMap edges** (`data/raw_osm_edges.csv`)  
- **Weather observations** (`data/raw_weather.csv`)  

Run the following script to merge, clean, prune non-pedestrian segments, impute missing values, normalize attributes, and export:

python scripts/preprocess_edges.py
python scripts/graph_model.py


import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/edges_normalized.csv')


for col in ['risk', 'scenic', 'weather']:
    df[f'n_{col}'] = df[col] / df[col].max()


alpha, beta, gamma = 0.5, 0.3, 0.2


G = nx.DiGraph()
for _, row in df.iterrows():
    cost = (
        alpha * row['n_risk'] +
        beta  * (1 - row['n_scenic']) +
        gamma * row['n_weather']
    )
    G.add_edge(
        row['u'], row['v'],
        length=row['length'],
        risk=row['n_risk'],
        scenic=row['n_scenic'],
        weather=row['n_weather'],
        cost=cost
    )


source_node, target_node = 'A', 'C'  # replace with real IDs
route = nx.shortest_path(G, source_node, target_node, weight='cost')
total_cost = sum(G[u][v]['cost'] for u, v in zip(route, route[1:]))

print(f"Optimal route from {source_node} to {target_node}: {route}")
print(f"Total cost: {total_cost:.3f}")

pos = nx.spring_layout(G)  # or use node coordinates if available
plt.figure(figsize=(8, 6))
nx.draw(G, pos, node_size=10, edge_color='lightgray')
nx.draw_networkx_nodes(G, pos, nodelist=route, node_color='red', node_size=50)
nx.draw_networkx_edges(
    G, pos,
    edgelist=list(zip(route, route[1:])),
    edge_color='red', width=2
)
plt.title('Example Optimal Dog-Walking Route')
plt.axis('off')
plt.tight_layout()
plt.savefig('assets/route_example.png', dpi=150)

python scripts/plot_descriptive.py

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/edges_normalized.csv')

plt.figure()
plt.hist(data['n_risk'],    bins=20, alpha=0.6, label='Risk')
plt.hist(data['n_scenic'],  bins=20, alpha=0.6, label='Scenic')
plt.hist(data['n_weather'], bins=20, alpha=0.6, label='Weather')
plt.xlabel('Score Value')
plt.ylabel('Frequency')
plt.title('Distribution of Edge Risk, Scenic, and Weather Scores')
plt.legend()
plt.tight_layout()
plt.savefig('assets/figure1_histogram.png', dpi=150)
![Figure 1: Distribution of Edge Risk, Scenic, and Weather Scores](/docs/assets/figure1_histogram.png)

python scripts/plot_comparison.py


import pandas as pd
import matplotlib.pyplot as plt


data = pd.DataFrame({
    'Distance (km)':       [2.50, 2.80, 3.00],
    'Risk Exposure':       [1.24, 0.81, 1.05],
    'Scenic Score Sum':    [78,   70,   95],
    'Weather Penalty Sum': [0.75, 0.80, 0.90]
}, index=['Baseline', 'Safety-Optimized', 'Scenic-Optimized'])

ax = data.plot(kind='bar')
ax.set_xlabel('Route Type')
ax.set_ylabel('Metric Value')
ax.set_title('Comparative Route Metrics')
plt.tight_layout()
plt.savefig('assets/figure2_comparison.png', dpi=150)
![Figure 2: Comparative Route Metrics](/docs/assets/figure2_comparison.png)


git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
cd <YOUR_REPO>
python scripts/preprocess_edges.py
python scripts/graph_model.py
python scripts/plot_descriptive.py
python scripts/plot_comparison.py
