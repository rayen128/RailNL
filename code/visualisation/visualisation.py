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
    # assert that state is an instance of State
    assert isinstance(
        state, State), "The input state must be an instance of State."

    # assert that state.stations exists and is a list
    assert hasattr(state, 'stations') and isinstance(
        state.stations, list), "State must have a 'stations' attribute that is a list."

    # assert that each station has a 'name', 'x', and 'y' attribute
    assert all(hasattr(station, 'name') and hasattr(station, 'x') and hasattr(station, 'y')
               for station in state.stations), "Each station must have 'name', 'x', and 'y' attributes."

    # assert that 'x' and 'y' attributes of each station are numeric
    assert all(isinstance(station.x, (int, float)) and isinstance(station.y, (int, float))
               for station in state.stations), "The 'x' and 'y' attributes of each station must be numeric."

    station_names = []
    station_dict = {}

    # add information to the list(s) and/or dict(s)
    for station in state.stations:
        station_names.append(station.name)
        station_dict[str(station.name)] = [float(station.y), float(station.x)]

    return station_names, station_dict


def plot_stations(p: figure, station_dict: dict[str: list[float]]) -> None:
    """
    explanation of method/function

    pre: 
        p is a (bokeh) figure
        coordinates are within display range of plot 
        station_dict is a dictionary
        all station_dict keys are strings
        all station_dict values are floats

    post:
        GeoJSON-data structure containing all stations and coordinates is created 
        all stations are plotted (and displayed) on the given figure       
    """

    # assert that p is an instance of Bokeh's Figure class
    assert isinstance(
        p, figure), "p must be an instance of Bokeh's Figure class."

    # assert that station_dict is a dictionary
    assert isinstance(station_dict, dict), "station_dict must be a dictionary."

    # assert that all keys in station_dict are strings
    assert all(isinstance(key, str) for key in station_dict.keys()
               ), "All keys in station_dict must be strings."

    # Assuming the structure of the values in station_dict, assert that each value is a list of two floats
    assert all(isinstance(coord, list) and len(coord) == 2 and all(isinstance(coord_value, float) for coord_value in coord)
               for coord in station_dict.values()), "Each value in station_dict must be a list of two floats."

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

    # plot the cities
    p.circle(x='x', y='y', size=7, color='Color',
             alpha=0.7, source=station_geo_source)


def plot_connections(p: figure, state: 'State', station_dict: dict[str: list[float]]) -> None:
    """
    explanation of method/function

    pre: 
        p is a (bokeh) figure
        coordinates are within display range of plot 
        station_dict is a dictionary
        all station_dict keys are strings
        all station_dict values are floats

    post:
        GeoJSON-data structure containing all connections with given coordinates and stations is created 
        all connections are plotted (and displayed) on the given figure       
    """

    # assert that p is an instance of Bokeh's Figure class
    assert isinstance(
        p, figure), "p must be an instance of Bokeh's Figure class."

    # assert that station_dict is a dictionary
    assert isinstance(station_dict, dict), "station_dict must be a dictionary."

    # assert that all keys in station_dict are strings
    assert all(isinstance(key, str) for key in station_dict.keys()
               ), "All keys in station_dict must be strings."

    # Assuming the structure of the values in station_dict, assert that each value is a list of two floats
    assert all(isinstance(coord, list) and len(coord) == 2 and all(isinstance(coord_value, float) for coord_value in coord)
               for coord in station_dict.values()), "Each value in station_dict must be a list of two floats."

    # create basis of GeoJSON-like structure
    connection_data = {
        'type': 'FeatureCollection',
        'features': []
    }

    # fill GeoJSON with all connections
    for connection in state.connections:

        # get connection coordinates
        start_coords = station_dict[connection.station_1.name]
        end_coords = station_dict[connection.station_2.name]

        # generate connection JSON object
        current_connection = {
            'type': 'Feature',
                    'geometry': {
                        'type': 'LineString',
                        'coordinates': [start_coords, end_coords]
                    },
            'properties': {
                        'Station1': f'{connection.station_1}',
                        'Station2': f'{connection.station_2}'
                    }
        }

        # add to connection_data
        connection_data['features'].append(current_connection)

    # create a GeoJSONDataSource for connections
    connection_geo_source = GeoJSONDataSource(
        geojson=json.dumps(connection_data))

    # plot connections
    p.multi_line(xs='xs', ys='ys', line_color='black',
                 source=connection_geo_source)


def plot_map(p: figure) -> None:
    """
    TODO: doc-string
    explanation of method/function

    pre: 
        pre-condition 1
        pre-condition 2

    post:
        post-condition 1
        post-condition 2

    returns:
        return_value 1
        return_value 2       
    """

    # Read GeoJSON file
    with open('../../data/nl_regions.geojson', 'r') as geojson_file:
        geojson_data = json.load(geojson_file)

    # Create GeoJSONDataSource
    map_geo_source = GeoJSONDataSource(geojson=json.dumps(geojson_data))

    # Plot the map using patches (polygons)
    p.patches('xs', 'ys', source=map_geo_source,
              line_color='black', fill_alpha=0.5)


def show_plot(station_dict: dict[str: list[float]], state: object) -> None:
    """
    TODO: doc-string
    explanation of method/function

    pre: 
        pre-condition 1
        pre-condition 2

    post:
        post-condition 1
        post-condition 2

    returns:
        return_value 1
        return_value 2       
    """

    # create a Bokeh figure
    p = figure(background_fill_color="lightgrey", tooltips=[
               ('Region', '@RegionName')])

    plot_map(p)
    plot_connections(p, state, station_dict)
    plot_stations(p, station_dict)

    # TODO: Hovers fixen regio's, connecties en stations allemaal hun losse hovers hebben
    # TODO: 'Lege connecties' in stations verwijderen (mogelijk al opgelost als hierboven gefixt is)
    # TODO: Optie voor Holland/Netherlands of andere (totaal nieuwe) optie toevoegen
    # TODO: Zorgen dat (gemaakte) routes er op komen (Denk legenda, verschillende kleurjes, RIJDENDE TREINEN?!?!?!)

    # add HoverTool for connections
    hover_connections = HoverTool(
        tooltips=[('Station 1', '@Station1'), ('Station 2', '@Station2')])
    p.add_tools(hover_connections)

    # show the plot
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
    show_plot(station_dict, state)
