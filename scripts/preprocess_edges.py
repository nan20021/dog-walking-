import pandas as pd

osm = pd.read_csv('data/raw_osm_edges.csv')
weather = pd.read_csv('data/raw_weather.csv')

def normalize(col): return col / col.max()
merged = pd.DataFrame({
    'u': osm.u, 'v': osm.v,
    'length': osm.length,
    'risk': normalize(osm.risk),
    'scenic': normalize(osm.scenic),
    'weather': normalize(weather.penalty)
})
merged.to_csv('data/edges_normalized.csv', index=False)
