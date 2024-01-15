from sys import argv, path
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
path.append("../classes")
from state import State
import os

from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure, show
from bokeh.sampledata.sample_geojson import geojson
import json


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
    station_dict = {}

    # add information to the list(s) and/or dict(s)
    for station in state.stations:
        station_names.append(station.name)
        station_dict[str(station.name)] = [station.y, station.x]

    return station_names, station_dict


def show_plot_bokeh(station_dict: dict[str: list[float]], state: object) -> None:
    # Create GeoJSON-like structure
    station_data = {
        'type': 'FeatureCollection',
        'features': [{'type': 'Feature',
                      'geometry': {'type': 'Point', 'coordinates': [lon, lat]},
                      'properties': {'StationName': city, 'Color': 'blue'}}
                     for city, [lon, lat] in station_dict.items()]
    }

    # Create GeoJSON-like structure for connections
    connection_data = {
        'type': 'FeatureCollection',
        'features': [{'type': 'Feature',
                      'geometry': {'type': 'LineString', 'coordinates': [[start_lon, start_lat], [end_lon, end_lat]]},
                      'properties': {'Station1': station_1, 'Station2': station_2}}
                     for (station_1, [start_lat, start_lon]), (station_2, [end_lat, end_lon]) in zip(station_dict.items(), station_dict.items())]
    }

    print(connection_data)

    # Add the created GeoJSON-like data
    for i in range(len(station_data['features'])):
        station_data['features'][i]['properties']['Color'] = 'red'

    # Create a GeoJSONDataSource
    geo_source = GeoJSONDataSource(geojson=json.dumps(station_data))

    # Create a Bokeh figure
    p = figure(background_fill_color="lightgrey", tooltips=[
               ('Station', '@StationName')])

    # Plot the cities
    p.circle(x='x', y='y', size=15, color='Color',
             alpha=0.7, source=geo_source)

    # Plot connections
    for connection in state.connections:
        start_coords = station_dict[connection.station_1.name]
        end_coords = station_dict[connection.station_2.name]

        p.segment(x0=start_coords[0], y0=start_coords[1],
                  x1=end_coords[0], y1=end_coords[1], line_color='black')

    # Show the plot
    show(p)


if __name__ == "__main__":

    # make sure a .csv is given for both stations and connections
    assert len(
        argv) == 2 or len(argv) == 3, "Usage: python3 representation.py [holland/netherlands] (optional) [directory]"

    # check if first argument is proper input
    assert argv[1].lower() == 'holland' or argv[
        1].lower() == 'netherlands', "Usage: python3 representation.py [holland/netherlands] (optional) [directory]"

    # make State object based on CL-input
    if argv[1].lower() == 'holland':
        state = State('../../data/stations_holland.csv',
                      '../../data/routes_holland.csv', 7, 120)
    elif argv[1].lower() == 'netherlands':
        state = State('../../data/stations_netherlands.csv',
                      '../../data/routes_netherlands.csv', 7, 120)

    # save coordinates and names
    station_names, station_dict = get_station_info(state)

    # create and show plot
    show_plot_bokeh(station_dict, state)
