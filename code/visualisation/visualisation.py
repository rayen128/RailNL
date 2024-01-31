from sys import argv, path
path.append("../classes")
from state import State
from route import Route
from connection import Connection
import os

from bokeh.models import GeoJSONDataSource, HoverTool, Legend
from bokeh.plotting import figure, show
from bokeh.sampledata.sample_geojson import geojson
from bokeh.palettes import Dark2_5 as palette
from bokeh.io import export_png
import itertools
import json


def get_station_info(state: object) -> dict[str: list[float]]:
    """ 
    gets all info regarding the stations in a state-object

    pre: 
        state input is State-object
        state.stations exists and contains Station-objects 
        all station has a name, x and y

    returns:  
        a dict with key = station_name and value = list[y-coordinate, x-coordinate]
    """
    # assert that state is an instance of State
    assert isinstance(
        state, object), "The input state must be an instance of State."

    # assert that state.stations exists and is a list
    assert hasattr(state, 'stations') and isinstance(
        state.stations, list), "State must have a 'stations' attribute that is a list."

    # assert that each station has a 'name', 'x', and 'y' attribute
    assert all(hasattr(station, 'name') and hasattr(station, 'x') and hasattr(station, 'y')
               for station in state.stations), "Each station must have 'name', 'x', and 'y' attributes."

    # assert that 'x' and 'y' attributes of each station are numeric
    assert all(isinstance(station.x, (int, float)) and isinstance(station.y, (int, float))
               for station in state.stations), "The 'x' and 'y' attributes of each station must be numeric."

    station_dict = {}

    # add information to the list(s) and/or dict(s)
    for station in state.stations:
        station_dict[str(station.name)] = [float(station.y), float(station.x)]

    return station_dict


def plot_stations(p: figure, station_dict: dict[str: list[float]]) -> None:
    """
    plots all stations based on related coordinates

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

    # assuming the structure of the values in station_dict, assert that each value is a list of two floats
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
    plots all connections based on related coordinates

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
                 source=connection_geo_source, name='Connections')


def plot_routes(p: figure, state: 'State', station_dict: dict[str: list[float]]) -> None:
    """
    plots all routes based on related coordinates

    pre: 
        p is a (bokeh) figure
        coordinates are within display range of plot 
        station_dict is a dictionary
        all station_dict keys are strings
        all station_dict values are floats

    post:
        GeoJSON-data structure containing all routes with given connections and stations is created 
        all routes are plotted (and displayed) on the given figure       
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

    colors = (
        "#ff0000", "#00ff00", "#0000ff", "#ffa500", "#ffff00",
        "#800080", "#008080", "#ffc0cb", "#00ffff", "#ff6347",
        "#7fff00", "#8a2be2", "#ffd700", "#32cd32", "#ff4500",
        "#9370db", "#00fa9a", "#ff1493", "#7cfc00", "#9932cc"
    )

    for i, route in enumerate(state.routes):
        # create basis of GeoJSON-like structure
        route_data = {
            'type': 'FeatureCollection',
            'features': []
        }

        for connection in route.route_connections:
            # get connection coordinates
            start_coords = station_dict[connection.station_1.name]
            end_coords = station_dict[connection.station_2.name]

            # generate connection JSON object
            current_route = {
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
            route_data['features'].append(current_route)

        # create a GeoJSONDataSource for connections
        current_route_geo_source = GeoJSONDataSource(
            geojson=json.dumps(route_data))

        # plot connections
        p.multi_line(xs='xs', ys='ys', legend_label=f"{route.name}: {route.route_stations[0]} - {route.route_stations[len(route.route_stations)-1]}",
                     line_width=3, line_color=colors[i % 20],
                     source=current_route_geo_source, name='Route')

    # display legend in top left corner (default is top right corner)
    p.add_layout(p.legend[0], "right")

    # add a title to your legend
    p.legend.title = "Routes"
    p.legend.click_policy = "hide"


def plot_map(p: figure, map: str) -> None:
    """
    plots the outline of a map based on a GeoJSON-file

    pre: 
        valid map string or GeoJSON-file adres is provided

    post:
        netherlands map is plotted on the given figure
    """

    if map == 'holland':
        with open('data/holland_regions.geojson', 'r') as geojson_file:
            geojson_data = json.load(geojson_file)

        # Create GeoJSONDataSource
        map_geo_source = GeoJSONDataSource(geojson=json.dumps(geojson_data))

        # Plot the map using patches (polygons)
        p.patches('xs', 'ys', source=map_geo_source,
                  line_color='black', fill_alpha=0.5)

    elif map == 'netherlands':
        # Read GeoJSON file
        with open('data/nl_regions.geojson', 'r') as geojson_file:
            geojson_data = json.load(geojson_file)

        # Create GeoJSONDataSource
        map_geo_source = GeoJSONDataSource(geojson=json.dumps(geojson_data))

        # Plot the map using patches (polygons)
        p.patches('xs', 'ys', source=map_geo_source,
                  line_color='black', fill_alpha=0.5)


def show_plot(station_dict: dict[str: list[float]], state: object, map: str) -> None:
    """
    completely plots the current state with stations, connections, routes and maps.

    pre: 
        station_dict is correctly initialized using the get_station_info function
        state is correctly intialized
        map is either holland or netherlands

    post:
        visualisation.html is created in the current map
        plot will automatically be opened 
    """

    # create a Bokeh figure
    p = figure(background_fill_color="lightgrey", width=1000, height=600)

    plot_map(p, map)
    plot_connections(p, state, station_dict)
    plot_routes(p, state, station_dict)
    plot_stations(p, station_dict)

    # TODO: Totale Score (goed) weergeven in de Legenda?

    # add HoverTool for connections
    hover_connections = HoverTool(
        renderers=[p.select_one({'name': 'Connections'})],
        tooltips=[('Station 1', '@Station1'), ('Station 2', '@Station2')])
    p.add_tools(hover_connections)

    # show the plot
    show(p)


if __name__ == "__main__":

    # make sure a .csv is given for both stations and connections
    assert len(
        argv) == 2 or len(argv) == 3, "Usage: python3 representation.py [holland/netherlands]"

    case_name = argv[1].lower()

    # check if first argument is proper input
    assert case_name == 'holland' or case_name == 'netherlands', "Usage: python3 visualisation.py [holland/netherlands]"

    # make State object based on CL-input
    if case_name == 'holland':
        state = State('../../data/stations_holland.csv',
                      '../../data/routes_holland.csv', 7, 120)

    elif case_name == 'netherlands':
        state = State('../../data/stations_netherlands.csv',
                      '../../data/routes_netherlands.csv', 20, 180)

    # state.add_route(state.connections[0])
    # state.add_route(state.connections[1])
    state.awaken_state('8438.0	1.0	7	862.0	False;False;True	train_1:Rotterdam Alexander>Gouda>Alphen a/d Rijn>Leiden Centraal>Schiphol Airport>Amsterdam Zuid>Amsterdam Sloterdijk>Zaandam>Amsterdam Sloterdijk>Amsterdam Centraal>Amsterdam Amstel>Amsterdam Centraal>Amsterdam Sloterdijk;train_2:Amsterdam Zuid>Schiphol Airport>Leiden Centraal>Den Haag Centraal>Gouda>Rotterdam Alexander>Gouda>Rotterdam Alexander>Rotterdam Centraal>Schiedam Centrum>Delft>Den Haag Centraal;train_3:Alkmaar>Hoorn>Zaandam>Beverwijk>Castricum>Alkmaar>Castricum>Zaandam>Castricum>Alkmaar;train_4:Delft>Den Haag Centraal>Leiden Centraal>Heemstede-Aerdenhout>Haarlem>Amsterdam Sloterdijk>Zaandam>Hoorn>Zaandam>Amsterdam Sloterdijk>Amsterdam Centraal;train_5:Amsterdam Zuid>Amsterdam Sloterdijk>Amsterdam Zuid>Schiphol Airport>Leiden Centraal>Heemstede-Aerdenhout>Haarlem>Amsterdam Sloterdijk>Amsterdam Zuid>Amsterdam Amstel>Amsterdam Zuid>Amsterdam Sloterdijk;train_6:Den Haag Centraal>Leiden Centraal>Alphen a/d Rijn>Leiden Centraal>Heemstede-Aerdenhout>Leiden Centraal>Den Haag Centraal>Delft>Schiedam Centrum>Rotterdam Centraal>Dordrecht;train_7:Amsterdam Sloterdijk>Haarlem>Beverwijk>Zaandam>Castricum>Alkmaar>Den Helder')

    # save coordinates and names
    station_dict = get_station_info(state)

    # create and show plot
    show_plot(station_dict, state, case_name)
