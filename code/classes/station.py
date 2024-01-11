class Station():

    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y
        self.connections: list[object] = []

    def add_connection(self, connection: object):
        self.connections.append(connection)
