import copy
from collections import deque
from itertools import combinations
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

    def kruskal_mst(self):
        edges = [(cost, u, v) for (u, v), cost in self.costs.items()]
        edges.sort()  #sortez
        ds = DisjointSet(self.number_of_vertices)
        mst = []
        total_cost = 0
        for cost, u, v in edges:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst.append((u, v, cost))
                total_cost += cost
                if len(mst) == self.number_of_vertices - 1:
                    break
        return mst, total_cost

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

    def find_connected_components(self):
        visited = set()
        components = []

        # Ensure we check every vertex, not just those with outgoing edges
        all_vertices = set(self.__outgoing_edges.keys()) | set(self.__incoming_edges.keys())

        for vertex in all_vertices:
            if vertex not in visited:
                component = self.bfs(vertex, visited)
                components.append(component)

        return components

    def bfs(self, start_vertex, visited):
        queue = deque([start_vertex])
        component = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                component.append(vertex)

                # Consider both incoming and outgoing edges to simulate an undirected graph
                neighbours = set(self.__outgoing_edges[vertex]) | set(self.__incoming_edges[vertex])
                for neighbour in neighbours:
                    if neighbour not in visited:
                        queue.append(neighbour)

        return component

    def tarjan_strongly_connected_components(self):
        """
        Find and return the list of strongly connected components
        using Tarjan's algorithm.
        """
        index = 0  # Number of nodes visited
        stack = []
        on_stack = set()  # Keep track of nodes on stack
        indices = {}  # Depth index of each node
        low_link = {}  # Lowest vertex reachable
        sccs = []  # List to hold the strongly connected components

        def strongconnect(vertex):
            nonlocal index, stack, on_stack, indices, low_link, sccs
            indices[vertex] = index
            low_link[vertex] = index
            index += 1
            stack.append(vertex)
            on_stack.add(vertex)

            for w in self.__outgoing_edges[vertex]:
                if w not in indices:
                    strongconnect(w)
                    low_link[vertex] = min(low_link[vertex], low_link[w])
                elif w in on_stack:
                    low_link[vertex] = min(low_link[vertex], indices[w])

            if low_link[vertex] == indices[vertex]:
                scc = []
                w = -1
                while w != vertex:
                    w = stack.pop()
                    on_stack.remove(w)
                    scc.append(w)
                sccs.append(scc)

        for v in range(self.__number_of_vertices):
            if v not in indices:
                strongconnect(v)

        return sccs

    def bellman_ford(self, source):
        """
        Bellman-Ford algorithm to find the shortest path from a source vertex to all other vertices in the graph
        and detect negative weight cycles that are reachable from the source.

        :param source: The source vertex
        :return: Tuple containing two elements:
                 - A dictionary of distances from the source to each vertex.
                 - A boolean indicating whether a negative cycle was detected.
        """
        # Initialize distances with infinity, and distance to source as 0
        distance = {vertex: float('inf') for vertex in self.parse_vertices()}
        distance[source] = 0

        # Relax edges up to V-1 times
        for _ in range(self.number_of_vertices - 1):
            for u, v in self.parse_cost():
                if distance[u] + self.costs[(u, v)] < distance[v]:
                    distance[v] = distance[u] + self.costs[(u, v)]

        # Check for negative weight cycles
        for u, v in self.parse_cost():
            if distance[u] + self.costs[(u, v)] < distance[v]:
                return (distance, True)

        return (distance, False)

    def bellman_ford1(self, source):
        """
        Bellman-Ford algorithm extended to find the shortest path from a source vertex to all other vertices in the graph,
        track the path, and detect negative weight cycles that are reachable from the source.

        :param source: The source vertex
        :return: Tuple containing three elements:
                 - A dictionary of distances from the source to each vertex.
                 - A dictionary with the path from the source to each vertex.
                 - A boolean indicating whether a negative cycle was detected.
        """
        # Initialize distances and predecessors
        distance = {vertex: float('inf') for vertex in self.parse_vertices()}
        predecessor = {vertex: None for vertex in self.parse_vertices()}
        distance[source] = 0

        # Relax edges up to V-1 times
        for _ in range(self.number_of_vertices - 1):
            for u, v in self.parse_cost():
                if distance[u] + self.costs[(u, v)] < distance[v]:
                    distance[v] = distance[u] + self.costs[(u, v)]
                    predecessor[v] = u

        # Check for negative weight cycles
        for u, v in self.parse_cost():
            if distance[u] + self.costs[(u, v)] < distance[v]:
                return (distance, predecessor, True)

        return (distance, predecessor, False)

    def find_all_min_cost_paths(self, start, end):
        from heapq import heappop, heappush
        from collections import defaultdict

        # vertices along with current cost
        pq = []
        heappush(pq, (0, start))

        # distances
        distances = defaultdict(lambda: float('inf'))
        distances[start] = 0

        # paths count
        path_count = defaultdict(int)
        path_count[start] = 1

        while pq:
            current_cost, current_vertex = heappop(pq)

            # stopping if we reach the destination
            if current_vertex == end:
                continue

            for neighbor in self.parse_outbound_edges(current_vertex):
                edge_cost = self.costs[(current_vertex, neighbor)]
                new_cost = current_cost + edge_cost

                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    path_count[neighbor] = path_count[current_vertex]
                    heappush(pq, (new_cost, neighbor))
                elif new_cost == distances[neighbor]:
                    path_count[neighbor] += path_count[current_vertex]

        return distances[end], path_count[end] if end in path_count else 0

    def topological_sort(self):
        from collections import deque
        in_degree = {i: 0 for i in range(self.number_of_vertices)}
        for v in self.parse_vertices():
            for neighbor in self.parse_outbound_edges(v):
                in_degree[neighbor] += 1

        # Queue for vertices with no incoming edges
        queue = deque([v for v in in_degree if in_degree[v] == 0])
        top_order = []

        while queue:
            vertex = queue.popleft()
            top_order.append(vertex)
            for neighbor in self.parse_outbound_edges(vertex):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(top_order) != self.number_of_vertices:
            return None  # This means there was a cycle, which shouldn't happen in a DAG
        return top_order

    def is_dag(self):
        """
        Verifies if the graph is a Directed Acyclic Graph (DAG).
        Returns True if it is a DAG, otherwise False.
        """
        return self.topological_sort() is not None

    def count_paths(self, start, end):
        """
        Finds the number of distinct paths between two given vertices in a DAG.
        Assumes the graph is a DAG.
        """
        # Perform topological sorting of the graph
        top_order = self.topological_sort()
        if top_order is None:
            return 0  # Cycle detected, invalid input for DAG

        # Path count array
        path_count = [0] * self.number_of_vertices
        path_count[start] = 1  # Start vertex has one way to "reach itself"

        for vertex in top_order:
            if path_count[vertex] > 0:
                for neighbor in self.parse_outbound_edges(vertex):
                    path_count[neighbor] += path_count[vertex]

        return path_count[end]

    def count_paths(self, start, end):
        # Perform topological sorting of the graph
        top_order = self.topological_sort()
        if top_order is None:
            return 0  # Cycle detected, invalid input for DAG

        # Path count array
        path_count = [0] * self.number_of_vertices
        path_count[start] = 1  # Start vertex has one way to "reach itself"

        for vertex in top_order:
            if path_count[vertex] > 0:
                for neighbor in self.parse_outbound_edges(vertex):
                    path_count[neighbor] += path_count[vertex]

        return path_count[end]

    def find_lowest_cost_paths(self, start, end):
        from heapq import heappop, heappush
        from collections import defaultdict

        top_order = self.topological_sort()
        if top_order is None:
            return 0, 0  # Cycle detected, invalid input for DAG

        distances = {vertex: float('inf') for vertex in self.parse_vertices()}
        path_count = {vertex: 0 for vertex in self.parse_vertices()}
        distances[start] = 0
        path_count[start] = 1

        for vertex in top_order:
            for neighbor in self.parse_outbound_edges(vertex):
                edge_cost = self.costs[(vertex, neighbor)]
                new_cost = distances[vertex] + edge_cost
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    path_count[neighbor] = path_count[vertex]
                elif new_cost == distances[neighbor]:
                    path_count[neighbor] += path_count[vertex]

        return distances[end], path_count[end]



class BridgeGraph(Graph):
    def __init__(self, crossing_times):
        super().__init__(len(crossing_times), 0)  # Initialize with persons as vertices
        self.crossing_times = crossing_times
        self.vertices = []

    def generate_all_states(self):
        #  all possible states of people on one side and the torch
        all_people = set(range(len(self.crossing_times)))
        for count in range(len(self.crossing_times) + 1):
            for people in combinations(all_people, count):
                self.vertices.append((frozenset(people), True))  # on original side
                self.vertices.append((frozenset(people), False)) # on the other side

    def find_neighbors(self, state):
        current_side, torch_position = state
        other_side = set(range(len(self.crossing_times))) - current_side

        neighbors = []
        if torch_position:  # Torch is on the original side
            possible_moves = combinations(current_side, 2) if len(current_side) > 1 else [(p,) for p in current_side]
        else:
            possible_moves = combinations(other_side, 1)  #one person returns with the torch

        for move in possible_moves:
            new_side = set(current_side).symmetric_difference(move)
            move_cost = max(self.crossing_times[p] for p in move)  #  slowest person in the move
            new_state = (frozenset(new_side), not torch_position)
            neighbors.append((new_state, move_cost))

        return neighbors

    def solve_bridge_problem(self):
        from heapq import heappush, heappop
        pq = []
        start_state = (frozenset(range(len(self.crossing_times))), True)
        heappush(pq, (0, start_state))  # (cost, state)
        visited = {}
        while pq:
            cost, state = heappop(pq)
            if state[0] == frozenset() and not state[1]:  # torch on the other side
                print(f"Solution found with cost {cost}")
                return cost
            if state in visited and visited[state] <= cost:
                continue
            visited[state] = cost
            for neighbor, move_cost in self.find_neighbors(state):
                next_cost = cost + move_cost
                if neighbor not in visited or visited[neighbor] > next_cost:
                    heappush(pq, (next_cost, neighbor))
        return float('inf')




class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

#pb 5 and 7 for lab 4, 5


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def build_tree_pre_in(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder.pop(0) # First element in preorder is the root
    root = TreeNode(root_val)
    inorder_index = inorder.index(root_val) # Find the root in inorder and split the array

    root.left = build_tree_pre_in(preorder, inorder[:inorder_index])
    root.right = build_tree_pre_in(preorder, inorder[inorder_index + 1:])

    return root

def build_tree_post_in(postorder, inorder):
    if not postorder or not inorder:
        return None

    root_val = postorder.pop()
    root = TreeNode(root_val)
    inorder_index = inorder.index(root_val)

    root.right = build_tree_post_in(postorder, inorder[inorder_index + 1:])
    root.left = build_tree_post_in(postorder, inorder[:inorder_index])

    return root



def build_tree_pre_post(preorder, postorder):
    if not preorder or not postorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)
    if len(preorder) == 1:
        return root

    left_val = preorder[1]
    left_index = postorder.index(left_val)

    root.left = build_tree_pre_post(preorder[1:left_index + 2], postorder[:left_index + 1])
    root.right = build_tree_pre_post(preorder[left_index + 2:], postorder[left_index + 1:-1])

    return root