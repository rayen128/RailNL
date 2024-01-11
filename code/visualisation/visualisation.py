from sys import argv, path
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

path.append("../classes")
# os.chdir("../classes")
from state import State


def get_station_info(map: object) -> tuple[list[float], list[float], list[str], dict[str: list[float]]]:
    """ 
    pre: 
        - map input is map object
        - map.stations exists and contains stations 
        - every station has a name, x and y


    returns: 
        - 3 list containing the latitude, longitude and names of all stations 
        - 1 dict containing all this info
    """
    station_names = []
    info_dict = {}

    # add information to lists/dict
    for station in map.stations:
        station_names.append(station.name)
        info_dict[str(station.name)] = [station.y, station.x]

    return station_names, info_dict


def show_plot(station_names: list[str], info_dict: dict[str: list[float]]) -> None:
    """
    pre: 
        - station_names is a list of strings
        - info_dict is a dict:
            - the keys are 
            - the values are lists of 

    post:
        - 
    """

    # Create a Cartopy map with a EuroPP projection
    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.EuroPP()})

    # Set the extent to zoom in on the Netherlands
    # [min_longitude, max_longitude, min_latitude, max_latitude]
    ax.set_extent([3.2, 7.5, 50.7, 53.7])

    # Add country borders
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    # Add land background
    ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')

    # Plot station locations
    ax.scatter([info_dict[name][1] for name in station_names], [
               info_dict[name][0] for name in station_names], color='red')

    # Plot connections
    for connection in map.connections:
        start_coords = info_dict[connection.station_1]
        end_coords = info_dict[connection.station_2]
        ax.plot([start_coords[1], end_coords[1]], [start_coords[0],
                end_coords[0]], 'b--', transform=ccrs.PlateCarree())

    # Set title
    ax.set_title('Stations')

    # Save or display the plot
    plt.savefig('Map')


if __name__ == "__main__":

    # make sure a .csv is given for both stations and connections
    assert len(
        argv) == 3, "Usage: representation.py [file path stations.csv] [file path connections.csv]"

    # make Map object
    map = Map(argv[1], argv[2])

    # save coordinates and names
    station_names, info_dict = get_station_info(map)

    # create and show plot
    show_plot(station_names, info_dict)
