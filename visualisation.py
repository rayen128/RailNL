import matplotlib.pyplot as plt
from representation import Map
from sys import argv


def get_station_info(map: object) -> tuple[list[float], list[float], list[str], dict[str: list[float]]]:
    """ 
    pre: 
            - map input is (correctly initialized) map object

    post: 
            - returns 3 lists and 1 dict
    """
    # create objects
    lat = []
    long = []
    station_names = []
    info_dict = {}

    # add information to lists/dict
    for station in map.stations:

        lat.append(station.y)
        long.append(station.x)
        station_names.append(station.name)
        info_dict[str(station.name)] = [station.y, station.x]

    return lat, long, station_names, info_dict


def show_plot(lat: list, long: list, station_names: list, info_dict: dict[str: list[float]]) -> None:
    """
    doc-string nog maken :'(
    """

    # im = plt.imread("../nederland.png")
    # implot = plt.imshow(im)

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
    lat, long, station_names, info_dict = get_station_info(map)

    # create and show plot
    show_plot(lat, long, station_names, info_dict)
