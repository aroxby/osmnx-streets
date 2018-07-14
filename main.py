import osmnx as ox

def main():
    city = ox.gdf_from_place("Berkeley, California")
    ox.plot_shape(ox.project_gdf(city))

if __name__ == '__main__':
    main()