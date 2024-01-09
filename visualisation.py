import matplotlib.pyplot as plt
from representation import Map
from sys import argv


def get_information(map):
    # list with coordinates
    lat = []
    long = []
    station_names = []

    for station in map.stations:
        lat.append(station.y)
        long.append(station.x)
        station_names.append(station.name)

    return lat, long, station_names


if __name__ == "__main__":

    # make sure a .csv is given for both stations and routes
    assert len(
        argv) == 3, "Usage: representation.py [file path stations.csv] [file path routes.csv]"

    # make Map object
    map = Map(argv[1], argv[2])

    lat, long, station_names = get_information(map)

    plt.scatter(long, lat, color='red')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Stations in Holland')
    plt.show()
