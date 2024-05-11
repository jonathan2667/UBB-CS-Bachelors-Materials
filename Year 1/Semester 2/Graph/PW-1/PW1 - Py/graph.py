import copy

# Graph Class Definition
class Graph:
    # Initializer / Constructor
    def __init__(self, number_of_vertices, number_of_edges):
        # Initialize basic graph properties
        self.__number_of_vertices = number_of_vertices
        self.__number_of_edges = number_of_edges

        # Initialize edge storage structures
        self.__incoming_edges = {}
        self.__outgoing_edges = {}
        self.__costs = {}

        # Set up vertices with no edges
        for index in range(number_of_vertices):
            self.__incoming_edges[index] = []
            self.__outgoing_edges[index] = []

    # Setters for graph properties
    def set_number_of_vertices(self, number_of_vertices):
        self.__number_of_vertices = number_of_vertices

    def set_number_of_edges(self, number_of_edges):
        self.__number_of_edges = number_of_edges

    def set_incoming_edges(self, incoming_edges):
        self.__incoming_edges = incoming_edges

    def set_outgoing_edges(self, outgoing_edges):
        self.__outgoing_edges = outgoing_edges

    def set_costs(self, costs):
        self.__costs = costs

    # Vertex and edge parsers - Iterators
    def parse_vertices(self):
        vertices = list(self.__outgoing_edges.keys())
        for v in vertices:
            yield v

    def parse_inbound_edges(self, vertex):
        for y in self.__incoming_edges[vertex]:
            yield y

    def parse_outbound_edges(self, vertex):
        for y in self.__outgoing_edges[vertex]:
            yield y

    def parse_cost(self):
        keys = list(self.__costs.keys())
        for key in keys:
            yield key

    # Property getters for graph properties
    @property
    def number_of_vertices(self):
        return self.__number_of_vertices

    @property
    def number_of_edges(self):
        return self.__number_of_edges

    @property
    def incoming_edges(self):
        return self.__incoming_edges

    @property
    def outgoing_edges(self):
        return self.__outgoing_edges

    @property
    def costs(self):
        return self.__costs

    # Vertex and edge manipulation methods
    def add_vertex(self, vertex):
        # Adds a vertex if it doesn't already exist
        if vertex in self.__outgoing_edges.keys() and vertex in self.__incoming_edges.keys():
            return False
        self.__outgoing_edges[vertex] = []
        self.__incoming_edges[vertex] = []
        self.__number_of_vertices += 1
        return True

    def remove_vertex(self, vertex):
        # Removes a vertex and its related edges
        if vertex not in self.__outgoing_edges.keys() and vertex not in self.__incoming_edges.keys():
            return False

        # Process removals for both incoming and outgoing edges
        for v in list(self.__outgoing_edges.keys()):
            if vertex in self.__outgoing_edges[v]:
                self.__outgoing_edges[v].remove(vertex)
        for v in list(self.__incoming_edges.keys()):
            if vertex in self.__incoming_edges[v]:
                self.__incoming_edges[v].remove(vertex)

        # Remove the vertex itself
        self.__outgoing_edges.pop(vertex, None)
        self.__incoming_edges.pop(vertex, None)

        # Adjust costs and edges count
        for key in list(self.__costs.keys()):
            if key[0] == vertex or key[1] == vertex:
                self.__costs.pop(key)
                self.__number_of_edges -= 1

        self.__number_of_vertices -= 1
        return True

    def add_edge(self, x, y, cost):
        # Adds an edge with a cost between two vertices
        if x not in self.__outgoing_edges.keys() or y not in self.__outgoing_edges.keys():
            return False
        self.__outgoing_edges[x].append(y)
        self.__incoming_edges[y].append(x)
        self.__costs[(x, y)] = cost
        self.__number_of_edges += 1
        return True

    def remove_edge(self, x, y):
        # Removes an edge between two vertices
        if x not in self.__outgoing_edges.keys() or y not in self.__outgoing_edges.keys():
            return False
        self.__outgoing_edges[x].remove(y)
        self.__incoming_edges[y].remove(x)
        self.__costs.pop((x, y))
        self.__number_of_edges -= 1
        return True

    # Graph analysis methods
    def in_degree(self, vertex):
        # Returns the in-degree of a vertex
        if vertex not in self.__incoming_edges.keys():
            return -1
        return len(self.__incoming_edges[vertex])

    def out_degree(self, vertex):
        # Returns the out-degree of a vertex
        if vertex not in self.__outgoing_edges.keys():
            return -1
        return len(self.__outgoing_edges[vertex])

    def find_if_edge(self, x, y):
        # Checks if there is an edge from x to y and returns its cost if it exists
        if x in self.__incoming_edges[y]:
            return self.__costs[(x, y)]
        if y in self.__outgoing_edges[x]:
            return self.__costs[(x, y)]
        return False

    def change_cost(self, x, y, new_cost):
        # Changes the cost of an existing edge
        if (x, y) not in self.__costs.keys():
            return False
        self.__costs[(x, y)] = new_cost
        return True

    def copy_graph(self):
        # Returns a deep copy of the graph
        return copy.deepcopy(self)
