import csv


def str_to_list(string: str, delimiter: str = '~') -> list[float]:
    """
    converts inputted string with score floats and specific delimiters to a list

    returns:
        list of scores
    """
    score_list = string.split(delimiter)
    return [float(score) for score in score_list]


def read_csv(csv_filepath: str, id_name: str) -> dict:
    """
    reads csv file with states and saves every state in a dictionary
    saves a dictionary with all the states dictionaries with state id as key

    pre: 
        csv_filepath is a string with a excisting csv file

    post:
        makes a dictionary with all the states in dictionaries

    returns:
        the dictionary with all the states

    """
    # make dictionary for saving the states
    states_dict: dict = {}
    
    # add every row to the dictionary with state id as key
    with open(csv_filepath) as states:
        csv_reader = csv.DictReader(states)
        for row in csv_reader:
            states_dict[row[id_name]] = row

    return states_dict


def filter_states(states_dict: dict, variable: str, value: str) -> dict:
    """
    filters the dictionary with states based on the given variable and value

    pre:
        states_dict is a dictionary with dictionaries in it
        variable is a key in the dictionaries in the dictionary
        value is a value which exist as value with this key

    returns:
        a dictionary with only the states which satisfy the filter
    """

    # make a empty dictionary for the filtered states
    filtered_scores = {}

    # check for every key if the given key in the state has the given value
    for key, state in states_dict.items():
        if state[variable] == value:
            filtered_scores[key] = state

    return filtered_scores


def export_states(states_dict: dict, file_path: str) -> None:
    """
    makes a csv file with the given dictionary with states

    pre:
        states_dict is a dictionary with states dictionaries
        file_path is a path in the current directory

    post:   
        saves a csv file with all the values from the states
    """

    # make a list with the column names
    field_names = list(states_dict[list(states_dict.keys())[0]].keys())

    # make a list with all states
    states_list = []
    for state in states_dict.values():
        states_list.append(state)

    # write all states in csv
    with open(f'{file_path}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(states_list)


def all_scores(states_dict: dict) -> list:
    """
    makes a list with all the scores from every state

    pre: 
        states_dict is a dict with which maintains state dictionaries  

    returns:
        the list with scores
    """

    # make an empty list to save the scores into
    scores = []

    # add all the scores from every state to the list
    for state in states_dict.values():
        scores.append(int(round(float(state["score"]), 0)))

    return scores
