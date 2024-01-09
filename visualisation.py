import matplotlib.pyplot as plt
from representation import Map
from sys import argv


def get_station_info(map: object) -> tuple:

    # create lists
    lat = []
    long = []
    station_names = []

    # add information to lists
    for station in map.stations:

        lat.append(station.y)
        long.append(station.x)
        station_names.append(station.name)

    return lat, long, station_names


def show_plot(lat: list, long: list, station_names: list, map: object) -> None:

    info_dict = {}

    for station in map.stations:
        info_dict[str(station.name)] = [station.y, station.x]

    # make scatterplot
    plt.scatter(long, lat, color='red')

    # add connections
    for connection in map.routes:

        start_lat = info_dict[connection.station_1][0]
        start_long = info_dict[connection.station_1][1]

        end_lat = info_dict[connection.station_2][0]
        end_long = info_dict[connection.station_2][1]
        plt.plot([start_long, end_long], [start_lat, end_lat], 'b--')

    # axis title
    plt.title('Stations')

    # hide the axis (values)
    plt.axis('off')

    plt.savefig('Map')


if __name__ == "__main__":

    # make sure a csv is given for both stations and routes
    assert len(
        argv) == 3, "Usage: representation.py [file path stations.csv] [file path routes.csv]"

    # make Map object
    map = Map(argv[1], argv[2])

    # save coordinates and names
    lat, long, station_names = get_station_info(map)

    # create and show plot
    show_plot(lat, long, station_names, map)
