from edges import edges_main, edges_AB3, faculty_room1_ground, faculty_room2_ground, faculty_room1_first, faculty_room2_first, faculty_room1_second, faculty_room2_second, faculty_room1_third, faculty_room2_third
import os
import time

class Node:
    def __init__(self, value):
        self.fr1 = None
        self.fr2 = None
        self.value = value
        self.neighbors = []
        self.inner_graph = Graph()
        self.initialize_inner_graph()

    def initialize_inner_graph(self):
        attribute_name = f"edges_{self.value}"
        if hasattr(edges_module, attribute_name):
            edges = getattr(edges_module, attribute_name)
            self.inner_graph.initialize_with_edges(edges)
        else:
            self.inner_graph = Graph()

class Graph:
    def __init__(self, vertices=0):
        self.vertices = vertices
        self.nodes = {str(i): Node(str(i)) for i in range(vertices)}
        self.edges = []
    
    def initialize_with_edges(self, edges):
        for edge in edges:
            if isinstance(edge[0], tuple):
                for e in edge:
                    source, destination, weight = e
                    self.add_edge(source, destination, weight)
            else:
                source, destination, weight = edge
                self.add_edge(source, destination, weight)

    def add_edge(self, u, v, weight=1):
        if u not in self.nodes:
            self.nodes[u] = Node(u)
        if v not in self.nodes:
            self.nodes[v] = Node(v)

        self.nodes[u].neighbors.append((v, weight))
        self.nodes[v].neighbors.append((u, weight))
        self.edges.append((u, v, weight))

    def remove_edge_main(self, u, v):
        if u in self.nodes and v in self.nodes:
            self.nodes[u].neighbors = [(node, weight) for node, weight in self.nodes[u].neighbors if node != v]
            self.nodes[v].neighbors = [(node, weight) for node, weight in self.nodes[v].neighbors if node != u]
            self.edges = [edge for edge in self.edges if not (edge[0] == u and edge[1] == v) and not (edge[0] == v and edge[1] == u)]
        
        with open("edges.py", "w") as file:
            file.write("edges_main = [\n")
            for edge in self.edges:
                file.write(f"{str(edge)},\n")
            file.write("]\n")
            file.write("edges_AB3 = [\n")
            for edge in edges_AB3:
                file.write(f"{str(edge)},\n")
            file.write("]")
            file.write("\n")
            file.write(f"faculty_room1_ground = {faculty_room1_ground}\n")
            file.write(f"faculty_room2_ground = {faculty_room2_ground}\n")
            file.write(f"faculty_room1_first = {faculty_room1_first}\n")
            file.write(f"faculty_room2_first = {faculty_room2_first}\n")
            file.write(f"faculty_room1_second = {faculty_room1_second}\n")
            file.write(f"faculty_room2_second = {faculty_room2_second}\n")
            file.write(f"faculty_room1_third = {faculty_room1_third}\n")
            file.write(f"faculty_room2_third = {faculty_room2_third}\n")
      
        print("Edge removed successfully!")
        self.print_graph()

    def remove_edge_ab3(self, u, v, room):
        
        # Update the edges_AB3 list to remove the edge
        room_index = room - 1
        room_edges = edges_AB3[room_index]

        # Remove the edge from the specific room/floor
        for edge in room_edges:
            if (u, v) == edge[:2] or (v, u) == edge[:2]:
                room_edges.remove(edge)
                break  # Stop after finding the edge to avoid unnecessary iterations

        edges_AB3[room_index] = room_edges

        # Update the graph structure to remove the edge
        if u in self.nodes and v in self.nodes:
            self.nodes[u].neighbors = [(node, weight) for node, weight in self.nodes[u].neighbors if node != v]
            self.nodes[v].neighbors = [(node, weight) for node, weight in self.nodes[v].neighbors if node != u]
            self.edges = [edge for edge in self.edges if not (edge[0] == u and edge[1] == v) and not (edge[0] == v and edge[1] == u)]

        # Write the updated edges to the file
        with open("edges.py", "w") as file:
            file.write("edges_main = [\n")
            for edge in edges_main:
                file.write(f"{str(edge)},\n")
            file.write("]\n")
            
            file.write("edges_AB3 = [\n")
            for floor_edges in edges_AB3:
                file.write("[\n")
                for edge in floor_edges:
                    file.write(f"{str(edge)},\n")
                file.write("],\n")
            file.write("]\n")

            file.write(f"faculty_room1_ground = {faculty_room1_ground}\n")
            file.write(f"faculty_room2_ground = {faculty_room2_ground}\n")
            file.write(f"faculty_room1_first = {faculty_room1_first}\n")
            file.write(f"faculty_room2_first = {faculty_room2_first}\n")
            file.write(f"faculty_room1_second = {faculty_room1_second}\n")
            file.write(f"faculty_room2_second = {faculty_room2_second}\n")
            file.write(f"faculty_room1_third = {faculty_room1_third}\n")
            file.write(f"faculty_room2_third = {faculty_room2_third}\n")

        print("Edge removed successfully!")
        self.print_graph()
    
    def print_graph(self):
        print('------------------------------------------------------------------------------------------')
        print("Current graph with all locations:")
        for vertex in self.nodes:
            neighbors = self.nodes[vertex].neighbors
            if neighbors:
                print(f"{vertex}:{neighbors}")
        print('------------------------------------------------------------------------------------------')

    def dijkstra(self, start_vertex):
        import heapq

        distances = {v: float('inf') for v in self.nodes}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]
        predecessors = {v: None for v in self.nodes}
        visited = set()

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            for neighbor, weight in self.nodes[current_vertex].neighbors:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, predecessors

    def shortest_path(self, start_vertex, end_vertex):
        distances, predecessors = self.dijkstra(start_vertex)
        path = []
        current_vertex = end_vertex

        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = predecessors[current_vertex]

        if distances[end_vertex] == float('inf'):
            return f"No path from {start_vertex} to {end_vertex}"
        else:
            path_info = []
            for i in range(len(path) - 1):
                path_info.append((self.get_vertex_name(path[i]), self.get_vertex_name(path[i + 1]), self.get_weight(path[i], path[i + 1])))
            return path, distances[end_vertex], path_info

    def get_vertex_index(self, name):
        for index, node in self.nodes.items():
            if node.value == name:
                return index
        return None

    def get_vertex_name(self, index):
        return self.nodes[index].value if index in self.nodes else None

    def find_path(self, start_vertex, end_vertex):
        visited = set()
        all_paths = []

        def dfs_util(curr_vertex, end_vertex, path):
            visited.add(curr_vertex)
            if curr_vertex == end_vertex:
                all_paths.append(path[:])
            else:
                for neighbor, _ in self.nodes[curr_vertex].neighbors:
                    if neighbor not in visited:
                        path.append(neighbor)
                        dfs_util(neighbor, end_vertex, path)
                        path.pop()
            visited.remove(curr_vertex)

        dfs_util(start_vertex, end_vertex, [start_vertex])
        return all_paths

    def get_weight(self, u, v):
        for edge in self.edges:
            if (edge[0] == u and edge[1] == v) or (edge[0] == v and edge[1] == u):
                return edge[2]
        return None

    def graph_size(self):
        return self.vertices

    def get_neighbors(self, vertex):
        return self.nodes[vertex].neighbors if vertex in self.nodes else []
    
    def find_faculty(self, faculty_name):
        for vertex in self.nodes:
            if self.nodes[vertex].value == faculty_name:
                return vertex
        return None


def find_shortest_path(graph):
    graph.print_graph()
    start_vertex = input("Enter the location where you are: ")
    end_vertex = input("Enter the location you want to go: ")
    if start_vertex not in graph.nodes or end_vertex not in graph.nodes:
        print(f"One or both of the vertices ({start_vertex}, {end_vertex}) do not exist in the graph.")
    else:
        result = graph.shortest_path(start_vertex, end_vertex)
        if isinstance(result, str):  # Incorrect, should check the content of the path instead
            print(result)
        else:
            path, distance, path_info = result
            if distance == float('inf'):  # Check if the distance is infinite
                print(f"No path from {start_vertex} to {end_vertex}")
            else:
                print(f"Shortest path from {start_vertex} to {end_vertex} is: {path}")
                print(f"Distance: {distance}")
                print("Path Details:")
                for (src, dest, weight) in path_info:
                    print(f"From {src} to {dest} with weight {weight}")


def find_faculty_member_all_floors(graphs, faculty_name):
    floors = ['Ground Floor', 'First Floor', 'Second Floor', 'Third Floor']
    entrances = ['entrance1', 'entrance1', 'entrance1', 'entrance1']
    
    for i, graph in enumerate(graphs):
        fr1 = graph.fr1
        fr2 = graph.fr2
        
        current = fr1.head
        while current:
            if current.element == faculty_name:
                path = print_shortest_path(graph, entrances[i], 'FR1')
                print(f"The faculty member '{faculty_name}' is located in: {floors[i]} in faculty room 1")
                return
            current = current.next
        
        current = fr2.head
        while current:
            if current.element == faculty_name:
                path = print_shortest_path(graph, entrances[i], 'FR2')
                print(f"The faculty member '{faculty_name}' is located in: {floors[i]} in faculty room 2")
                return
            current = current.next
    
    print(f"The faculty member '{faculty_name}' was not found on any floor.")
    input("Press Enter to continue...")


def print_shortest_path(graph, start_vertex, end_vertex):
    if start_vertex not in graph.nodes or end_vertex not in graph.nodes:
        print(f"One or both of the vertices ({start_vertex}, {end_vertex}) do not exist in the graph.")
    else:
        result = graph.shortest_path(start_vertex, end_vertex)
        if isinstance(result, str):
            print(result)
        else:
            path, distance, path_info = result
            if distance == float('inf'):
                print(f"No path from {start_vertex} to {end_vertex}")
            else:
                print(f"Shortest path from {start_vertex} to {end_vertex} is: {path}")
                print(f"Distance: {distance}")
                print("Path Details:")
                for (src, dest, weight) in path_info:
                    print(f"From {src} to {dest} with weight {weight}")


def add_edge_main(graph):
    u = input("Enter the source vertex: ")
    v = input("Enter the destination vertex: ")
    w = int(input("Enter the weight: "))
    
    new_edge = (u, v, w)
    edges_main.append(new_edge)

    with open("edges.py", "w") as file:
        file.write("edges_main = [\n")
        for edge in edges_main:
            file.write(f"{str(edge)},\n")
        file.write("]\n\n")
        
        file.write("edges_AB3 = [\n")
        for edge in edges_AB3:
            file.write(f"{str(edge)},\n")
        file.write("]")

        file.write("\n")
        file.write(f"faculty_room1_ground = {faculty_room1_ground}\n")
        file.write(f"faculty_room2_ground = {faculty_room2_ground}\n")
        file.write(f"faculty_room1_first = {faculty_room1_first}\n")
        file.write(f"faculty_room2_first = {faculty_room2_first}\n")
        file.write(f"faculty_room1_second = {faculty_room1_second}\n")
        file.write(f"faculty_room2_second = {faculty_room2_second}\n")
        file.write(f"faculty_room1_third = {faculty_room1_third}\n")
        file.write(f"faculty_room2_third = {faculty_room2_third}\n")
    
    print("Edge added successfully!")
    graph.add_edge(u, v, w)
    graph.print_graph()


def print_graph_all(graph):
    graph.print_graph()


def delete_edge_main(graph):
    print('------------------------------------------------------------------------------------------')
    u = input("Enter the source vertex: ")
    v = input("Enter the destination vertex: ")
    print('------------------------------------------------------------------------------------------')
    graph.remove_edge_main(u, v)


def delete_edge_ab3(graph,room):
    print('------------------------------------------------------------------------------------------')
    u = input("Enter the source vertex: ")
    v = input("Enter the destination vertex: ")
    print('------------------------------------------------------------------------------------------')
    graph.remove_edge_ab3(u, v,room)


def add_edge_ab3(graph, room):
    u = input("Enter the source vertex: ")
    v = input("Enter the destination vertex: ")
    w = int(input("Enter the weight: "))
    
    new_edge = (u, v, w)
    edges_AB3[room-1].append(new_edge)

    with open("edges.py", "w") as file:
        file.write("edges_main = [\n")
        for edge in edges_main:
            file.write(f"{str(edge)},\n")
        file.write("]\n\n")
        
        file.write("edges_AB3 = [\n")
        for edge in edges_AB3:
            file.write(f"{str(edge)},\n")
        file.write("]")

        file.write("\n")
        file.write(f"faculty_room1_ground = {faculty_room1_ground}\n")
        file.write(f"faculty_room2_ground = {faculty_room2_ground}\n")
        file.write(f"faculty_room1_first = {faculty_room1_first}\n")
        file.write(f"faculty_room2_first = {faculty_room2_first}\n")
        file.write(f"faculty_room1_second = {faculty_room1_second}\n")
        file.write(f"faculty_room2_second = {faculty_room2_second}\n")
        file.write(f"faculty_room1_third = {faculty_room1_third}\n")
        file.write(f"faculty_room2_third = {faculty_room2_third}\n")
    
    print("Edge added successfully!")
    graph.add_edge(u, v, w)
    graph.print_graph()


# Import the edges module dynamically
import importlib.util
spec = importlib.util.spec_from_file_location("edges", "edges.py")
edges_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(edges_module)

# Initialize the main graph
main_graph = Graph(vertices=len(edges_main))
main_graph.initialize_with_edges(edges_main)

# Initialize inner graphs for each node in the main graph
for node in main_graph.nodes.values():
    node.initialize_inner_graph()