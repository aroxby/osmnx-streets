import osmnx as ox
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Stolen from https://github.com/gboeing/osmnx-examples/blob/3acb26f/notebooks/15-calculate-visualize-edge-bearings.ipynb
    G = ox.graph_from_place('Pittsburgh, Pennsylvania', network_type='drive')
    G = ox.add_edge_bearings(G)
    bearings = pd.Series([data['bearing'] for u, v, k, data in G.edges(keys=True, data=True)])

    # polar plot# polar
    n = 30
    count, division = np.histogram(bearings, bins=[ang*360/n for ang in range(0,n+1)])
    division = division[0:-1]
    width =  2 * np.pi/n
    ax = plt.subplot(111, projection='polar')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction('clockwise')
    bars = ax.bar(division * np.pi/180 - width * 0.5 , count, width=width, bottom=20.0)
    ax.set_title('Pittsburgh street network edge bearings', y=1.1)
    plt.show()

if __name__ == '__main__':
    main()