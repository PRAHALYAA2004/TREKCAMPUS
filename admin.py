import time
from edges import edges_main, edges_AB3,faculty_room1_ground,faculty_room2_ground,faculty_room1_first,faculty_room2_first,faculty_room2_second,faculty_room1_second,faculty_room2_third,faculty_room1_third
import os
import time
from faculty import dlist
from graph import Graph,Node,find_shortest_path,find_faculty_member_all_floors,print_shortest_path,add_edge_main,print_graph_all,delete_edge_main,add_edge_ab3,delete_edge_ab3

def admin_menu():
    admin_password = input("Enter the admin password: ")
    while True:
        if admin_password == "admin123":
            print('''
-----------------------------------------
▄▀█ █▀▄ █▀▄▀█ █ █▄░█   █▀▄▀█ █▀▀ █▄░█ █░█
█▀█ █▄▀ █░▀░█ █ █░▀█   █░▀░█ ██▄ █░▀█ █▄█
-----------------------------------------''')
            print("1. Campus navigation")
            print("2. Building navigation")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")
            print('-----------------------------------------')
            if choice == "1":
                admin_campus_navigation()
            elif choice == "2":
                admin_building_navigation()
            elif choice == "3":
                print("\nReturning to user/admin selection\n", end="")
                for _ in range(3):
                    time.sleep(1)
                    print(".", end="", flush=True)
                print("\n")
                break
            else:
                print("\nInvalid choice. Please try again.\n")
        else:
            print("Invalid password. Please try again.")

def admin_campus_navigation():
    vertices = 56
    graph = Graph(vertices)
    graph.initialize_with_edges(edges_main)
    while True:
        print('''
---------------------------------------------------------------------------------------
▄▀█ █▀▄ █▀▄▀█ █ █▄░█   █▀▀ ▄▀█ █▀▄▀█ █▀█ █░█ █▀   █▄░█ ▄▀█ █░█ █ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█
█▀█ █▄▀ █░▀░█ █ █░▀█   █▄▄ █▀█ █░▀░█ █▀▀ █▄█ ▄█   █░▀█ █▀█ ▀▄▀ █ █▄█ █▀█ ░█░ █ █▄█ █░▀█
---------------------------------------------------------------------------------------
''')

        print("1. Add edges")
        print("2. Remove edges")
        print("3. Print graph")
        print("4. Exit")
        print('--------------------------------------------------------------------------------------------')


        ch = input("Enter your choice (1-4): ")

        if ch == "1":
            add_edge_main(graph)
        elif ch == "2":
            delete_edge_main(graph)
        elif ch == "3":
            print_graph_all(graph)
        elif ch == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def admin_building_navigation():
    def initialize_dlist(faculty_room):
        dl = dlist()
        for member in faculty_room:
            dl.insertlast(member)
        return dl

    faculty_room1_ground_list = initialize_dlist(faculty_room1_ground)
    faculty_room2_ground_list = initialize_dlist(faculty_room2_ground)

# Now you can use these lists for your operations

    print('--------------------------------------------------------------------------------------------')
    print("Available buildings for navigation:")
    print("1. AB3")
    print('--------------------------------------------------------------------------------------------')

    building_choice = input("Enter the building you want to navigate (e.g., AB3): ").strip().upper()

    if building_choice != "AB3":
        print("Invalid building choice. Returning to main menu.")
        return

    while True:
        print('''
--------------------------------------------------------------------------------------------
▄▀█ █▀▄ █▀▄▀█ █ █▄░█   █▄▄ █░█ █ █░░ █▀▄ █ █▄░█ █▀▀   █▄░█ ▄▀█ █░█ █ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█
█▀█ █▄▀ █░▀░█ █ █░▀█   █▄█ █▄█ █ █▄▄ █▄▀ █ █░▀█ █▄█   █░▀█ █▀█ ▀▄▀ █ █▄█ █▀█ ░█░ █ █▄█ █░▀█
--------------------------------------------------------------------------------------------''')

        print("1. Ground Floor")
        print("2. First Floor")
        print("3. Second Floor")
        print("4. Third Floor")
        print("5. Exit")
        print("--------------------------------------------------------------------------------------------")

        floor_choice = input("Enter the floor number (1/2/3/4):")

        if floor_choice == '5':
            break

        elif floor_choice in ['1', '2', '3', '4']:
            floor_index = int(floor_choice) - 1
            floor_edges = edges_AB3[floor_index]
            vertices = 56
            graph = Graph(vertices)
            graph.edges = floor_edges.copy()
            for u, v, w in floor_edges:
                graph.add_edge(u, v, w)

            if floor_choice == '1':
                room = "ground"
                f1 = faculty_room1_ground
                f2 = faculty_room2_ground
            elif floor_choice == '2':
                room = "first"
                f1 = faculty_room1_first
                f2 = faculty_room2_first
            elif floor_choice == '3':
                room = "second"
                f1 = faculty_room1_second
                f2 = faculty_room2_second
            elif floor_choice == '4':
                room = "third"
                f1 = faculty_room1_third
                f2 = faculty_room2_third

            graph.fr1 = dlist()
            graph.fr2 = dlist()

            for faculty in f1:
                graph.fr1.insertlast(faculty)
            for faculty in f2:
                graph.fr2.insertlast(faculty)

            while True:
                print('--------------------------------------------------------------------------------------------')
                print(f"{['Ground Floor', 'First Floor', 'Second Floor', 'Third Floor'][floor_index]}")
                print("1. Add edges")
                print("2. Remove edges")
                print("3. Print graph")
                print("4. Add Faculty")
                print("5. Remove Faculty")
                print("6. Faculty list for a floor")
                print("7. Exit")
                print('--------------------------------------------------------------------------------------------')
                ch = input("Enter your choice (1-7): ")

                if ch == "1":
                    add_edge_ab3(graph, floor_index + 1)
                elif ch == "2":
                    delete_edge_ab3(graph, int(floor_choice))
                elif ch == "3":
                    print_graph_all(graph)
                elif ch == "4":
                    room_choice = input("Enter the room (fr1 or fr2): ")
                    name = input("Enter the faculty name: ")
                    position = input("Enter the position (first/last/0-9): ")

                    if room_choice == "fr1":
                        graph.fr1.add_faculty(name, position, floor_index, room_choice)
                    elif room_choice == "fr2":
                        graph.fr2.add_faculty(name, position, floor_index, room_choice)
                    else:
                        print("Invalid room choice.")
                elif ch == "5":
                    room_choice = input("Enter the room (fr1 or fr2): ")
                    name = input("Enter the faculty name: ")

                    if room_choice == "fr1":
                        graph.fr1.remove_faculty(name, floor_index, room_choice)
                    elif room_choice == "fr2":
                        graph.fr2.remove_faculty(name, floor_index, room_choice)
                    else:
                        print("Invalid room choice.")
                elif ch == "6":
                    print("Faculty room 1 teacher's list")
                    graph.fr1.printlist()
                    print("Faculty room 2 teacher's list")
                    graph.fr2.printlist()
                elif ch == "7":
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid floor choice. Please try again.")
