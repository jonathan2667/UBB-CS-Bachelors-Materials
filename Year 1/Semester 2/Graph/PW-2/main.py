from random import randint

from graph import Graph


def write_graph_to_file(graph, filename):
    """
    Writes a graph to a file
    :param graph:
    :param filename:
    :return:
    """
    file = open(filename, "w")
    if graph.number_of_edges and graph.number_of_vertices:
        file.write(str(graph.number_of_vertices) + " " + str(graph.number_of_edges) + "\n")
        if len(graph.costs) == 0 and len(graph.incoming_edges) == 0 and len(graph.outgoing_edges) == 0:
            raise ValueError("Graph is empty")
        for key in graph.costs.keys():
            file.write(str(key[0]) + " " + str(key[1]) + " " + str(graph.costs[key]) + "\n")
    else:
        first_line = 'We cannot create this graph' + '\n'
        file.write(first_line)
    file.close()




def read_modified_graph_from_file(filename):
    pass

def read_graph_from_file(filename):
    """
    Reads a graph from a file
    :param filename:
    :return:
    """
    file = open(filename, "r")
    line = file.readline()
    line = line.strip()
    vertices, edges = line.split(' ')
    graph = Graph(int(vertices), int(edges))
    line = file.readline().strip()
    while len(line) > 0:
        line = line.split(' ')
        if len(line) == 1:
            graph.incoming_edges[int(line[0])] = []
            graph.outgoing_edges[int(line[0])] = []
        elif len(line) == 3:
            graph.incoming_edges[int(line[1])].append(int(line[0]))
            graph.outgoing_edges[int(line[0])].append(int(line[1]))
            graph.costs[(int(line[0]), int(line[1]))] = int(line[2])
        line = file.readline().strip()
    file.close()
    return graph

class UI:
    def __init__(self):
        self._graphs = []
        self._current = None


    def generate_random(self, vertices, edges):
        """
        Generates a random graph
        :param vertices:
        :param edges:
        :return:
        """
        graph = Graph(vertices, 0)
        i = 0
        while i < edges:
            x = randint(0, vertices - 1)
            y = randint(0, vertices - 1)
            cost = randint(0, 500)
            if graph.add_edge(x, y, cost):
                i += 1
        return graph

    def switch_graph_ui(self):
        """
        Switches the current graph
        :return:
        """
        print("You are on the graph number: {}".format(self._current))
        print("Available graphs: from 0 - {}".format(str(len(self._graphs) - 1)))
        number = int(input("Enter the graph number you want to switch to: "))
        if not 0 <= number < len(self._graphs):
            raise ValueError("Trying to switch to a non existing graph!")
        self._current = number

    def add_empty_graph(self):
        """
        Adds an empty graph
        :return:
        """
        if self._current is None:
            self._current = 0
        graph = Graph(0, 0)
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1

    def create_random_graph_ui(self):
        """
        Creates a random graph
        :return:
        """
        vertices = int(input("Enter the number of vertices: "))
        edges = int(input("Enter the number of edges: "))
        if edges > vertices * vertices:
            graph = Graph(0, 0)
            print("Too many edges!")
        else:
            graph = self.generate_random(vertices, edges)
        if self._current is None:
            self._current = 0
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1

    def get_number_of_vertices_ui(self):
        """
        Prints the number of vertices
        :return:
        """
        print("The number of vertices is: {}.".format(self._graphs[self._current].number_of_vertices))

    def get_number_of_edges_ui(self):
        """
        Prints the number of edges
        :return:
        """
        print("The number of edges is: {}.".format(self._graphs[self._current].number_of_edges))

    def list_all_outbound(self):
        """
        Lists all the outbound edges of the graph
        :return:
        """
        for x in self._graphs[self._current].parse_vertices():
            line = str(x) + " :"
            for y in self._graphs[self._current].parse_outbound_edges(x):
                line = line + " " + str(y)
            print(line)

    def list_outbound(self):
        """
        Lists the outbound edges of a given vertex
        :return:
        """
        vertex = int(input("Enter the vertex: "))
        line = str(vertex) + " :"
        if vertex not in self._graphs[self._current].parse_vertices():
            raise ValueError("Cannot list outbound of this vertex, it does not exist!")
        for y in self._graphs[self._current].parse_outbound_edges(vertex):
            line = line + " " + "({}, {})".format(str(vertex), str(y))
        print(line)

    def list_all_inbound(self):
        """
        Lists all the inbound edges of the graph
        :return:
        """
        for x in self._graphs[self._current].parse_vertices():
            line = str(x) + " :"
            for y in self._graphs[self._current].parse_inbound_edges(x):
                line = line + " " + str(y)
            print(line)

    def list_inbound(self):
        """
        Lists the inbound edges of a given vertex
        :return:
        """
        vertex = int(input("Enter the vertex: "))
        line = str(vertex) + " :"
        if vertex not in self._graphs[self._current].parse_vertices():
            raise ValueError("Cannot list inbound of this vertex, it does not exist!")
        for y in self._graphs[self._current].parse_inbound_edges(vertex):
            line = line + " " + "({}, {})".format(str(y), str(vertex))
        print(line)

    def list_all_costs(self):
        """
        Lists all the edges and their costs
        :return:
        """
        for key in self._graphs[self._current].parse_cost():
            line = "({}, {})".format(key[0], key[1]) + " :" + str(self._graphs[self._current].costs[key])
            print(line)

    def parse_all_vertices(self):
        """
        Parses all the vertices
        :return:
        """
        for vertex in self._graphs[self._current].parse_vertices():
            print("{}".format(vertex))

    def add_vertex_ui(self):
        """
        Adds a vertex
        :return:
        """
        vertex = int(input("Enter the new vertex: "))
        added = self._graphs[self._current].add_vertex(vertex)
        if added:
            print("Vertex added successfully!")
        else:
            print("Cannot add this vertex, it already exists!")

    def delete_vertex_ui(self):
        """
        Deletes a vertex
        :return:
        """
        vertex = int(input("Enter the vertex to be deleted: "))
        deleted = self._graphs[self._current].remove_vertex(vertex)
        if deleted:
            print("Vertex deleted successfully!")
        else:
            print("Cannot delete this vertex, it does not exist!")

    def add_edge_ui(self):
        """
        Adds an edge
        :return:
        """
        print("Add an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        cost = int(input("Enter the cost of the edge: "))
        added = self._graphs[self._current].add_edge(vertex_x, vertex_y, cost)
        if added:
            print("Edge added successfully!")
        else:
            print("Cannot add this edge, it already exists!")

    def remove_edge_ui(self):
        """
        Removes an edge
        :return:
        """
        print("Remove an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        deleted = self._graphs[self._current].remove_edge(vertex_x, vertex_y)
        if deleted:
            print("Edge deleted successfully!")
        else:
            print("Cannot remove this edge, it does not exist!")

    def modify_cost_ui(self):
        """
        Modifies the cost of an edge
        :return:
        """
        print("Modify the cost of an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        cost = int(input("Enter the cost of the edge: "))
        changed = self._graphs[self._current].change_cost(vertex_x, vertex_y, cost)
        if changed:
            print("Cost modified successfully!")
        else:
            print("Cannot modify the cost, the edge does not exist!")

    def get_in_degree_ui(self):
        """
        Gets the in degree of a vertex
        :return:
        """
        vertex = int(input("Enter the vertex:"))
        degree = self._graphs[self._current].in_degree(vertex)
        if degree == -1:
            print("The vertex does not exist!")
        else:
            print("The in degree of the vertex {} is {}.".format(vertex, degree))

    def get_out_degree_ui(self):
        """
        Gets the out degree of a vertex
        :return:
        """
        vertex = int(input("Enter the vertex:"))
        degree = self._graphs[self._current].out_degree(vertex)
        if degree == -1:
            print("The vertex does not exist!")
        else:
            print("The out degree of the vertex {} is {}.".format(vertex, degree))

    def check_if_edge_ui(self):
        """
        Checks if there is an edge between two vertices
        :return:
        """
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        edge = self._graphs[self._current].find_if_edge(vertex_x, vertex_y)
        if edge is not False:
            print("({}, {}) is an edge and its cost is {}!".format(vertex_x, vertex_y, edge))
        else:
            print("({}, {}) is not an edge!".format(vertex_x, vertex_y))


    def copy_current_graph_ui(self):
        """
        Makes a copy of the current graph
        :return:
        """
        copy = self._graphs[self._current].copy_graph()
        self._graphs.append(copy)

    def read_graph_from_file_ui(self):
        """
        Reads a graph from a file
        :return:
        """
        filename = input("Enter the name of the file: ")
        if self._current is None:
            self._current = 0
        graph = read_graph_from_file(filename)
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1

    def write_graph_to_file_ui(self):
        """
        Writes the graph to a file
        :return:
        """
        current_graph = self._graphs[self._current]
        output_file = "random_graph" + str(self._current) + ".txt"
        write_graph_to_file(current_graph, output_file)

    def read_modified_graph_from_file_ui(self):
        """
        Reads a modified graph from a file
        :return:
        """
        filename = input("Enter the name of the file: ")
        if self._current is None:
            self._current = 0
        graph = read_modified_graph_from_file(filename)
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1

    def write_modified_graph_to_file_ui(self):
        """
        Writes the modified graph to a file
        :return:
        """
        current_graph = self._graphs[self._current]
        output_file = "graph_modif" + str(self._current) + ".txt"
        write_graph_to_file(current_graph, output_file)

    def get_connected_components_ui(self):
        # Assuming self._graphs[self._current] is an instance of the Graph class
        components = self._graphs[self._current].find_connected_components()
        print("Found {} connected component(s).".format(len(components)))
        for i, component in enumerate(components):
            print("Component {}: {}".format(i + 1, component))


    def find_strongly_connected_components_ui(self):
        print("Finding strongly connected components of the current graph...")
        sccs = self._graphs[self._current].tarjan_strongly_connected_components()
        print(f"Found {len(sccs)} strongly connected component(s).")
        for i, component in enumerate(sccs):
            print(f"Component {i + 1}: {component}")

    def print_menu(self):
        """
        Prints the menu
        :return:
        """
        print("""
                📊 Graph Operations Menu
                ---------------------
                0️⃣ Exit

                🏗️ Graph Initialization
                1️⃣ Create a random graph with specified number of vertices and edges. 
                2️⃣ Read the graph from a text file.
                3️⃣ Write the graph in a text file. 
                4️⃣ Switch the graph. 
                5️⃣ Add an empty graph.

                🔍 Graph Properties
                6️⃣ Get the number of vertices.
                7️⃣ Get the number of edges.
                8️⃣ Get the in degree of a vertex.
                9️⃣ Get the out degree of a vertex.
                🔟 Parse all the vertices.

                🛠️ Edge and Vertex Operations
                1️⃣1️⃣ Add a vertex. 
                1️⃣2️⃣ Remove a vertex. 
                1️⃣3️⃣ Add an edge. 
                1️⃣4️⃣ Remove an edge. 
                1️⃣5️⃣ Modify the cost of an edge. 

                📈 Graph Analysis
                1️⃣6️⃣ List the outbound edges of a given vertex.
                1️⃣7️⃣ List all outbound vertices of the graph.
                1️⃣8️⃣ List the inbound edges of a given vertex.
                1️⃣9️⃣ List all inbound vertices of the graph.
                2️⃣0️⃣ List the edges and their costs.
                2️⃣1️⃣ Check if there is an edge between two given vertices. 
                2️⃣2️⃣ Make a copy of the graph. 
                
                
                🔍Modified Files
                2️⃣3️⃣ Write the modified graph in a text file.
                
                
                📈 Pw-2
                2️⃣4️⃣ Get the connected components of the graph.
                2️⃣5️⃣ Get the strongly connected components of the graph.
                """)

    def start(self):
        print("Welcome!")
        done = False
        self.add_empty_graph()
        print("The current graph is an empty graph!")
        command_dict = {"1": self.create_random_graph_ui,
                        "2": self.read_graph_from_file_ui,
                        "3": self.write_graph_to_file_ui,
                        "4": self.switch_graph_ui,
                        "5": self.add_empty_graph,
                        "6": self.get_number_of_vertices_ui,
                        "7": self.get_number_of_edges_ui,
                        "8": self.get_in_degree_ui,
                        "9": self.get_out_degree_ui,
                        "10": self.parse_all_vertices,
                        "11": self.add_vertex_ui,
                        "12": self.delete_vertex_ui,
                        "13": self.add_edge_ui,
                        "14": self.remove_edge_ui,
                        "15": self.modify_cost_ui,
                        "16": self.list_outbound,
                        "17": self.list_all_outbound,
                        "18": self.list_inbound,
                        "19": self.list_all_inbound,
                        "20": self.list_all_costs,
                        "21": self.check_if_edge_ui,
                        "22": self.copy_current_graph_ui,
                        "23": self.write_modified_graph_to_file_ui,
                        "24": self.get_connected_components_ui,
                        "25": self.find_strongly_connected_components_ui
                        }
        while not done:
            try:
                self.print_menu()
                option = input("Enter a command from the menu: \n")
                if option == "0":
                    done = True
                elif option in command_dict:
                    command_dict[option]()
                else:
                    print("Try again!\n")
            except Exception as e:
                print(str(e))


UI().start()

#PB 5 LAB 3