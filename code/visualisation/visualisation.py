from sys import argv, path
path.append("../classes")
from state import State
import os

from bokeh.models import GeoJSONDataSource, HoverTool
from bokeh.plotting import figure, show
from bokeh.sampledata.sample_geojson import geojson
from itertools import product
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

    # create GeoJSON-like structure
    station_data = {
        'type': 'FeatureCollection',
        'features': [{'type': 'Feature',
                      'geometry': {'type': 'Point', 'coordinates': [lon, lat]},
                      'properties': {'StationName': city, 'Color': 'red'}}
                     for city, [lon, lat] in station_dict.items()]
    }

    # create a GeoJSONDataSource
    station_geo_source = GeoJSONDataSource(geojson=json.dumps(station_data))

    connection_data = {
        'type': 'FeatureCollection',
        'features': []
    }

    for connection in state.connections:
        start_coords = station_dict[connection.station_1.name]
        end_coords = station_dict[connection.station_2.name]

        current_connection = {
            'type': 'Feature',
                    'geometry': {
                        'type': 'LineString',
                        'coordinates': [f"{start_coords}, {end_coords}"]
                    },
            'properties': {
                        'Station1': f'{connection.station_1}',
                        'Station2': f'{connection.station_2}'
                    }
        }

        connection_data['features'].append(current_connection)

    # create a GeoJSONDataSource for connections
    connection_geo_source = GeoJSONDataSource(
        geojson=json.dumps(connection_data))

    # create a Bokeh figure
    p = figure(background_fill_color="lightgrey", tooltips=[
               ('Station', '@StationName')])

    # plot the cities
    p.circle(x='x', y='y', size=15, color='Color',
             alpha=0.7, source=station_geo_source)

    # plot connections
    p.multi_line(x='x', y='y', line_color='black',
                 source=connection_geo_source)

    # add HoverTool for connections
    hover_connections = HoverTool(
        tooltips=[('Station 1', '@Station1'), ('Station 2', '@Station2')])
    p.add_tools(hover_connections)

    # show the plot
    # show(p)


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
