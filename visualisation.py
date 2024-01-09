import matplotlib.pyplot as plt
from representation import Map
from sys import argv


def get_information(map: object) -> tuple:

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


def show_plot(lat: list, long: list, station_names: list) -> None:

    # make scatterplot
    plt.scatter(long, lat, color='red')

    # axis title
    plt.title('Stations in Holland')

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
    lat, long, station_names = get_information(map)

    # create and show plot
    show_plot(lat, long, station_names)
