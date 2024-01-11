from sys import argv, path
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
path.append("../classes")
from state import State
import os


def get_station_info(state: object) -> tuple[list[str], dict[str: list[float]]]:
    """ 
    pre: 
        state input is State-object
        state.stations exists and contains Station-objects 
        all station has a name, x and y


    returns: 
        a list containing the names of all stations 
        a dict with key = station_name and value = list[y-coordinate, x-coordinate]
    """
    station_names = []
    info_dict = {}

    # add information to the list(s) and/or dict(s)
    for station in state.stations:
        station_names.append(station.name)
        info_dict[str(station.name)] = [station.y, station.x]

    return station_names, info_dict


def show_plot(station_names: list[str], info_dict: dict[str: list[float]], directory: str = '../../docs') -> None:
    """
    pre: 
        station_names is a list of strings
        info_dict is a dict
        keys of info_dict are strings    
        values of info_dict are list of floats 
        directory is a string
        specified directory exists


    post:
        saves picture of the Netherlands as 'map.png'
    """

    # assertion check for station_names
    assert all(isinstance(name, str)
               for name in station_names), "All elements in station_names must be strings."

    # assertions for info_dict
    assert isinstance(info_dict, dict), "info_dict must be a dictionary."

    assert all(isinstance(key, str) for key in info_dict.keys()
               ), "All keys in info_dict must be strings."

    assert all(isinstance(value, list) for value in info_dict.values()
               ), "All values in info_dict must be lists of floats."

    assert all(all(isinstance(num, float) for num in value)
               for value in info_dict.values()), "All values in info_dict lists must be floats."

    # assertion for directory
    assert isinstance(directory, str), "directory must be a string."

    # create a Cartopy map with a EuroPP projection
    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.EuroPP()})

    # set the extent to zoom in on the Netherlands
    # [min_longitude, max_longitude, min_latitude, max_latitude]
    ax.set_extent([3.2, 7.5, 50.7, 53.7])

    # add country borders
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    # add land background
    ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')

    # plot station locations
    ax.scatter([info_dict[name][1] for name in station_names], [
               info_dict[name][0] for name in station_names], color='red')

    # plot connections
    for connection in map.connections:
        start_coords = info_dict[connection.station_1]
        end_coords = info_dict[connection.station_2]
        ax.plot([start_coords[1], end_coords[1]], [start_coords[0],
                end_coords[0]], 'b--', transform=ccrs.PlateCarree())

    # set title
    ax.set_title('Stations')

    # save and check validity of (the potentially) specified directory
    directory = directory
    assert os.path.exists(directory), 'Given directory does not exist'

    # save or display the plot
    plt.savefig(f'{directory}/Map.png')


if __name__ == "__main__":

    # make sure a .csv is given for both stations and connections
    assert len(
        argv) == 2 or len(argv) == 3, "Usage: python3 representation.py [holland/netherlands] (optional) [directory]"

    # check if first argument is proper input
    assert argv[1].lower() == 'holland' or argv[
        1].lower == 'netherlands', "Usage: python3 representation.py [holland/netherlands] (optional) [directory]"

    # make State object based on CL-input
    if argv[1].lower() == 'holland':
        state = State('..\data\stations_holland.csv',
                      '..\data\routes_holland.csv')
    elif argv[1].lower() == 'netherlands':
        state = State('..\data\stations_netherlands.csv',
                      '..\data\routes_netherlands.csv')

    # save coordinates and names
    station_names, info_dict = get_station_info(state)

    # create and show plot
    show_plot(station_names, info_dict)
