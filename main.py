from sys import argv, path

path.append("code/classes")
from state import State

if __name__ == "__main__":

    # make sure a .csv is given for both stations and routes
    assert len(
        argv) == 3, "Usage: representation.py [file path stations.csv] [file path routes.csv]"

    # make Map object
    state: object = State(argv[1], argv[2])