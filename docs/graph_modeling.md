---
title: Methods & Implementation
---
# Methods & Implementation
python scripts/preprocess_edges.py
python scripts/graph_modeling.py
G = nx.DiGraph()
for _, row in df.iterrows():
    cost = alpha*row['risk'] + beta*(1–row['scenic']) + gamma*row['weather']
    G.add_edge(row['u'], row['v'], cost=cost)
docs/assets/route_example.png
![Example Optimal Route](assets/route_example.png)
[← Back to Home](index.html) • [Next: Results & Figures](results.html)
