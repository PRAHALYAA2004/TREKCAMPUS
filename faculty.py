class dlist:
    class Node:
        def __init__(self, e=None):
            self.element = e
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.max = 10

    def insertfirst(self, e):
        newnode = self.Node(e)
        if self.size == self.max:
            print("No availability of cabin")
            return
        if self.size == 0:
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.size += 1

    def insertlast(self, e):
        newnode = self.Node(e)
        if self.size == self.max:
            print("No availability of cabin")
            return
        if self.size == 0:
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.size += 1

    def insert_at_position(self, e, position):
        if position < 0 or position >= self.max:
            print("Invalid position")
            return

        newnode = self.Node(e)
        current = self.head
        for _ in range(position):
            if current is None:
                break
            current = current.next

        if current is None:
            if position == 0:
                self.insertfirst(e)
            else:
                print("Position out of range")
            return

        if current.element is None:
            current.element = e
            self.size += 1
        else:
            newnode.next = current.next
            newnode.prev = current
            current.next = newnode
            if newnode.next is not None:
                newnode.next.prev = newnode
            if newnode.next is None:
                self.tail = newnode
            self.size += 1

    def printlist(self):
        if self.size == 0:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.element + ' | ' if current.element else "Vacant | ", end=" ")
                current = current.next
            print()

    def add_faculty(self, name, position, floor_index, room_choice):
        if position == "first":
            self.insertfirst(name)
        elif position == "last":
            self.insertlast(name)
        else:
            try:
                position_index = int(position)
                current = self.head
                for _ in range(position_index):
                    if current is None:
                        break
                    current = current.next

                if current is not None and current.element is None:
                    current.element = name
                    self.size += 1
                else:
                    print("Not possible to add at the given position")
            except ValueError:
                print("Invalid position, must be 'first', 'last' or an integer")

        self.update_faculty_list(floor_index, room_choice)

    def remove_faculty(self, name, floor_index, room_choice):
        current = self.head
        while current:
            if current.element == name:
                current.element = None
                self.size -= 1
                self.update_faculty_list(floor_index, room_choice)
                print(f"Removed {name}. Current size: {self.size}")
                return
            current = current.next
        print(f"{name} not found in the list.")

    def update_faculty_list(self, floor_index, room_choice):
        room_names = ["ground", "first", "second", "third"]
        room = room_names[floor_index]
        faculty_room_str = f"faculty_room{room_choice[-1]}_{room}"

        with open("edges.py", "r") as file:
            lines = file.readlines()

        updated_lines = []
        for line in lines:
            if faculty_room_str in line:
                faculty_list = []
                current = self.head
                while current:
                    if current.element is not None:
                        faculty_list.append(f'"{current.element}"')
                    else:
                        faculty_list.append("None")
                    current = current.next
                updated_lines.append(f"{faculty_room_str} = [{', '.join(faculty_list)}]\n")
            else:
                updated_lines.append(line)

        with open("edges.py", "w") as file:
            file.writelines(updated_lines)

        print(f"Updated {faculty_room_str}")

