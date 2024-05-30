from edges import edges_main, edges_AB3, faculty_room1_ground, faculty_room2_ground, faculty_room1_first, faculty_room2_first, faculty_room2_second, faculty_room1_second, faculty_room2_third, faculty_room1_third
import os
import time
from faculty import dlist
from graph import Graph, Node, find_shortest_path, find_faculty_member_all_floors, print_shortest_path, print_graph_all


def user_menu():
    while True:
        print('''
-----------------------------------
█░█ █▀ █▀▀ █▀█   █▀▄▀█ █▀▀ █▄░█ █░█ 
█▄█ ▄█ ██▄ █▀▄   █░▀░█ ██▄ █░▀█ █▄█ 
-----------------------------------
1. Campus navigation
2. Building navigation
3. Exit
------------------------------------''')
        choice = input("Enter your choice (1-3): ")
        print('------------------------------------')
        if choice == "1":
            user_campus_navigation()
        elif choice == "2":
            user_building_navigation()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
            print('------------------------------------')

def user_campus_navigation():
    vertices = 54
    graph = Graph(vertices)
    graph.initialize_with_edges(edges_main)
    while True:
        print('''
---------------------------------------------------------------------------------
█░█ █▀ █▀▀ █▀█   █▀▀ ▄▀█ █▀▄▀█ █▀█ █░█ █▀   █▄░█ ▄▀█ █░█ █ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█
█▄█ ▄█ ██▄ █▀▄   █▄▄ █▀█ █░▀░█ █▀▀ █▄█ ▄█   █░▀█ █▀█ ▀▄▀ █ █▄█ █▀█ ░█░ █ █▄█ █░▀█
---------------------------------------------------------------------------------
1. Find shortest path
2. Print graph
3. Exit
---------------------------------------------------------------------------------''')

        ch = input("Enter your choice (1-3): ")
        
        if ch == "1":
            find_shortest_path(graph)
        elif ch == "2":
            print_graph_all(graph)
        elif ch == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def user_building_navigation():
    # Display available buildings
    print('---------------------------------------------------------------------------------')
    print("Available buildings for navigation:")
    print("1. AB3")
    print('---------------------------------------------------------------------------------')

    building_choice = input("Enter the building you want to navigate (e.g., AB3): ").strip().upper()

    if building_choice != "AB3":
        print("Invalid building choice. Returning to main menu.")
        return

    vertices = 56  # Assuming the number of vertices is the same for all floors
    graphs = []
    
    # Create Graph instances for each floor
    for floor_edges in edges_AB3:
        graph = Graph(vertices)
        graph.edges = floor_edges.copy()
        for u, v, w in floor_edges:
            graph.add_edge(u, v, w)
        graphs.append(graph)

    # Insert faculty lists into respective graphs
    for i, graph in enumerate(graphs):
        if i == 0:  # Ground Floor
            f1 = faculty_room1_ground
            f2 = faculty_room2_ground
        elif i == 1:  # First Floor
            f1 = faculty_room1_first
            f2 = faculty_room2_first
        elif i == 2:  # Second Floor
            f1 = faculty_room1_second
            f2 = faculty_room2_second
        elif i == 3:  # Third Floor
            f1 = faculty_room1_third
            f2 = faculty_room2_third

        graph.fr1 = dlist()
        graph.fr2 = dlist()

        for faculty in f1:
            graph.fr1.insertlast(faculty)
        for faculty in f2:
            graph.fr2.insertlast(faculty)

    while True:
        print('''
-------------------------------------------------------------------------------------
█░█ █▀ █▀▀ █▀█   █▄▄ █░█ █ █░░ █▀▄ █ █▄░█ █▀▀   █▄░█ ▄▀█ █░█ █ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█
█▄█ ▄█ ██▄ █▀▄   █▄█ █▄█ █ █▄▄ █▄▀ █ █░▀█ █▄█   █░▀█ █▀█ ▀▄▀ █ █▄█ █▀█ ░█░ █ █▄█ █░▀█
-------------------------------------------------------------------------------------
1. Ground Floor
2. First Floor
3. Second Floor
4. Third Floor
5. Find Faculty Member
6. Exit       
-------------------------------------------------------------------------------------''')




        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            break

        elif choice == '5':
            faculty_name = input("Enter the name of the faculty member: ")
            find_faculty_member_all_floors(graphs, faculty_name)

        elif choice in ['1', '2', '3', '4']:
            floor_index = int(choice) - 1
            graph = graphs[floor_index]

            while True:
                print('-------------------------------------------------------------------------------------')

                print(f"{['Ground Floor', 'First Floor', 'Second Floor', 'Third Floor'][floor_index]}")
                print("1. Find shortest path")
                print("2. Print graph")
                print("3. Print faculty list")
                print("4. Exit")
                print('-------------------------------------------------------------------------------------')

                ch = input("Enter your choice (1-4): ")

                if ch == "1":
                    find_shortest_path(graph)
                elif ch == "2":
                    print_graph_all(graph)
                elif ch == "3":
                    print("Faculty room 1 teacher's list in cabin order : ")
                    graph.fr1.printlist()
                    print("Faculty room 2 teacher's list in cabin order : ")
                    graph.fr2.printlist()
                elif ch == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid floor choice. Please try again.")


if __name__ == "__main__":
    user_menu()
    