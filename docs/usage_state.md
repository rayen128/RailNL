# Usage State object
## Intro
This document aims to give an overview of all the attributes and relations the basic data structure of our case has, so that it can be implemented easily.

## Initialization
The initialization of a State class looks like this:
```python
state = State(file_path_stations, file_path_connections, max_number_routes, time_frame)
```
The required parameters are the following:
- **file_path_stations**: an absolute or relative file path to the csv with stations;
- **file_path_connections**: an absolute or relative path to the csv with connections;
- **max_number_routes**: the maximum number of routes that can be implemented;
- **time_frame**: the maximum time in minutes a route can be.

The optional parameters are there for constraint relaxation, and are `False` by default.
- **relaxed_all_connections**: if `True`, not all connections need to be used for a valid option.
- **relaxed_max_routes**: if `True`, the max number of routes can be surpassed.
- **relaxed_time_frame**: if `True`, routes can exceed the timeframe.

## Variables
- all variables given in initialization
- **total_number_connections**: total number of connections the loaded case has. 
- **stations**: list of all Station objects
- **connections**: list of all Connection objects
- **routes**: list of all Route objects
- **max_number_routes**: max number of routes
- **quality**: quality score
- **fraction_used_connections**: total connections / used connections (used for quality score)
- **number_routes**: length of `routes` (used for quality score)
- **total_minutes**: total amount of time al routes take together (used for quality score)
- **route_id_tracker**: used to track route names

## Methods
### add_route
```python
state.add_route(-connection-)
```
This method adds a new route with the first start connection.

### delete_route
```python
state.delete_route(-route-)
```
This method removes given route.

### calculate_score
```python
state.calculate_score()
```
This method calculates and returns the quality score of the state.

### write_output
```python
state.write_output(-file_path-)
```
This method writes the output to a the given .csv file path.

### routes_valid_time_frame
```python
state.routes_valid_time_frame()
```
This methods returns whether all routes are in the timeframe or not.

### less_than_max_routes
```python
state.less_than_max_routes()
```
This method checks if the number of routes is less than the max.

### all_connections_used
```python
state.all_connections_used()
```
This methods checks whether all connections are used or not.

### is_valid_solution
```python
state.is_valid_solution()
```
This method checks if all constraints are satisfied (with use of three methods above), taking into account the constraint relaxation.


### is_valid_solution_non_relaxed
```python
state.is_valid_solution_non_relaxed()
```
This method does the above, **not** taking into account the constraint relaxation.

### show
```python
state.show()
```
This method returns a description of the state.

### show_sleeper_string
```python
state.show_sleeper_string()
```
This method returns a string that can activate this particular state at any given moment.

### awaken_state
```python
state.awaken_state(-sleeper_string-)
```
This method activates a state, using a sleeper string generated with the method above.

### show_csv_line
```python
state.show_csv_line(-state_id-, -algorithm-)
```
This method returns a string that can be embedded in a csv file with lots of others of these lines.

### reset
```python
state.reset()
```
This method resets the state.

## Related objects
### Route
The route object also has some relevant attributes. The Routes are stored in a list in the State. A route is initialized with the `add_route` method.

#### variables
- **name**: name of the route.
- **route_stations**: list of all stations in the route.
- **route_connections**: list of all connections in the route.
- **total_time**: time the route takes.

#### methods
##### get_start_station, get_end_station
```python
state.routes[index].get_start_station()
```
```python
state.routes[index].get_end_station()
```
Gives Station object of the start or end of the route.

##### add_connection
```pyhton
state.routes[index].add_connection(-connection-)
```
This method adds given connection to the route (if possible).

##### delete_connection_start, delete_connection_end
```python
state.routes[index].delete_connection_start()
```
```python
state.routes[index].delete_connection_end()
```
These methods delete the connection at the start or the end.

##### is_station_in_route
```python
state.routes[index].is_station_in_route(-station-)
```
This method checks if given Station is in the route.

##### is_connection_in_route
```python
state.routes[index].is_connection_in_route(-station-)
```
This method checks if given Connection is in the route.

##### is_valid_time
```python
state.routes[index].is_valid_time(-time_frame-)
```
This method checks if the time of Route is smaller than the given timeframe