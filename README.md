
#TREKCAMPUS

TrekCampus is an intra-campus navigation system designed to simplify campus navigation for students, faculty, and visitors. By providing real-time directions, point-to-point routes, and easy access to campus locations, TrekCampus enhances user experience and convenience within a campus environment.

## Features

- **Interactive Map:** Provides a detailed, interactive map of the campus.
- **Point-to-Point Navigation:** Calculates the optimal path between locations.
- **Real-Time Updates:** Updates routes based on campus conditions, events, or restricted areas.
- **Location Search:** Quickly search for buildings, facilities, and other points of interest on campus.
- **Faculty Management:** Supports adding and removing faculty members in various campus rooms, with dynamic list updates in campus files.
- **Admin Interface:** Allows administrators to modify campus and building navigation options and manage faculty room assignments.

## Getting Started

To set up TrekCampus on your local system, follow these steps:

### Prerequisites

- Python 3.x
- Required Python packages

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/TrekCampus.git
   ```

2. Navigate into the project directory:

   ```bash
   cd TrekCampus
   ```

3. Install any required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the main navigation script:

   ```bash
   python main.py
   ```

2. Use the interface to search for locations or get directions between points on campus.
3. Use the `faculty.py` functionalities to add or remove faculty members, and update their location data in `edges.py`.
4. Access the admin functions in `admin.py` to configure campus and building navigation and manage faculty room lists.

### Configuration

- **Campus Graph (edges.py):** This file defines the main campus routes (`edges_main`) and building-specific edges for `AB3` (`edges_AB3`) across different floors. Additionally, it contains `faculty_room` lists to hold faculty names for each room on different floors. This layout data is critical to navigation and building management functionalities.
- **Faculty Management (faculty.py):** Manages a doubly linked list of faculty members and updates their room assignments in `edges.py` dynamically.
- **Admin Functions (admin.py):** The central administration interface allows the addition and removal of edges for campus navigation, initialization and updating of faculty lists, and building-specific navigation configurations for different floors.

### Project Structure

```
TrekCampus/
│
├── main.py             # Entry point for the application
├── graph.py            # Contains graph-based data for campus locations and routes
├── user.py             # Handles user-related functionalities
├── faculty.py          # Manages faculty lists and updates room assignments in edges.py
├── admin.py            # Provides admin tools for campus/building navigation and faculty management
├── edges.py            # Defines main campus routes, building routes, and faculty room data
├── README.md           # Project documentation
```

### Faculty and Admin Management

The `faculty.py` file includes the `dlist` class, which provides the following functionalities for faculty management:

- **Adding Faculty:** Use `add_faculty(name, position, floor_index, room_choice)` to add a faculty member to a specific position in the doubly linked list. The room assignment in `edges.py` will be updated based on the `floor_index` and `room_choice`.
- **Removing Faculty:** Use `remove_faculty(name, floor_index, room_choice)` to remove a faculty member from the list and update the room data in `edges.py`.
- **Updating Faculty List:** The `update_faculty_list(floor_index, room_choice)` method automatically updates room occupancy in `edges.py` to reflect the current state of the faculty list.

The `admin.py` file includes the following main functionalities:

- **Campus and Building Navigation:** Allows the admin to add, remove, and view edges in the campus navigation graph, as well as manage building-specific navigation for each floor.
- **Faculty Management:** Enables the admin to initialize faculty lists for each floor’s rooms, add or remove faculty members from specific rooms, and update the faculty data in `edges.py` accordingly.

## Contributing

We welcome contributions! If you have suggestions or improvements, please open a pull request or an issue.


---
