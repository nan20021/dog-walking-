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

