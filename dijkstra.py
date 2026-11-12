graph = {
    "Chitipa": [
        ("Karonga", 160)
    ],

    "Karonga": [
        ("Chitipa", 160),
        ("Rumphi", 130)
    ],

    "Rumphi": [
        ("Karonga", 130),
        ("Mzimba", 110),
        ("Nkhata Bay", 110)
    ],

    "Mzimba": [
        ("Rumphi", 110),
        ("Nkhata Bay", 60),
        ("Kasungu", 200)
    ],

    "Nkhata Bay": [
        ("Rumphi", 110),
        ("Mzimba", 60),
        ("Nkhotakota", 250)
    ],

    "Kasungu": [
        ("Mzimba", 200),
        ("Nkhotakota", 125),
        ("Dowa", 85),
        ("Lilongwe", 125)
    ],

    "Nkhotakota": [
        ("Nkhata Bay", 250),
        ("Kasungu", 125),
        ("Salima", 110)
    ],

    "Dowa": [
        ("Kasungu", 85),
        ("Lilongwe", 55)
    ],

    "Lilongwe": [
        ("Kasungu", 125),
        ("Dowa", 55),
        ("Salima", 100),
        ("Dedza", 85)
    ],

    "Salima": [
        ("Nkhotakota", 110),
        ("Lilongwe", 100),
        ("Mangochi", 120)
    ],

    "Mangochi": [
        ("Salima", 120),
        ("Balaka", 80),
        ("Zomba", 135)
    ],

    "Dedza": [
        ("Lilongwe", 85),
        ("Ntcheu", 60)
    ],

    "Ntcheu": [
        ("Dedza", 60),
        ("Balaka", 90)
    ],

    "Balaka": [
        ("Ntcheu", 90),
        ("Mangochi", 80),
        ("Zomba", 90),
        ("Blantyre", 130)
    ],

    "Zomba": [
        ("Balaka", 90),
        ("Blantyre", 65),
        ("Mulanje", 85),
        ("Mangochi", 135)
    ],

    "Blantyre": [
        ("Balaka", 130),
        ("Zomba", 65),
        ("Thyolo", 40),
        ("Chikwawa", 55)
    ],

    "Thyolo": [
        ("Blantyre", 40),
        ("Mulanje", 50)
    ],

    "Mulanje": [
        ("Zomba", 85),
        ("Thyolo", 50)
    ],

    "Chikwawa": [
        ("Blantyre", 55),
        ("Nsanje", 95)
    ],

    "Nsanje": [
        ("Chikwawa", 95)
    ]
}

#DIJKSTRA'S ALGORITHM
def dijkstra(graph, start, destination):

    # Checking if the towns exists in the graph
    if start not in graph or destination not in graph:
        print("Error: Town not found in the graph.")
        return

    # Store the shortest known distance to each town
    distances = {}

    # Store the previous town in the shortest route
    previous = {}

    # Initially, all towns have infinite distance
    for town in graph:
        distances[town] = float("inf")
        previous[town] = None

    # Distance from the starting town to itself is zero
    distances[start] = 0

    # All towns are initially unvisited
    unvisited = list(graph.keys())

    # Continue until all reachable towns are visited
    while unvisited:

        # Find the unvisited town with the smallest distance
        current_town = None
        smallest_distance = float("inf")

        for town in unvisited:
            if distances[town] < smallest_distance:
                smallest_distance = distances[town]
                current_town = town

        # Stop if the remaining towns cannot be reached
        if current_town is None:
            break

        # Remove the selected town from unvisited towns
        unvisited.remove(current_town)

        # Stop if we have reached our destination
        if current_town == destination:
            break

        # Examine all neighbouring towns
        for neighbour, road_distance in graph[current_town]:

            if neighbour in unvisited:

                # Calculate the new possible distance
                new_distance = (
                    distances[current_town] + road_distance
                )

                # Update if a shorter route is found
                if new_distance < distances[neighbour]:

                    distances[neighbour] = new_distance
                    previous[neighbour] = current_town

    # Check whether the destination was reachable
    if distances[destination] == float("inf"):
        print("No route exists between these towns.")
        return

    # reconstruction
    path = []
    current_town = destination

    while current_town is not None:
        path.append(current_town)
        current_town = previous[current_town]

    # Reverse the path to get the correct direction
    path.reverse()

    return distances[destination], path

# function for displaying the results
def display_result(start, destination):

    result = dijkstra(graph, start, destination)

    if result is None:
        return

    distance, path = result

    print("\nDIJKSTRA'S SHORTEST PATH")
    print("-----------------------------")
    print("Starting town:", start)
    print("Destination:", destination)

    print("Shortest route:")
    print(" -> ".join(path))

    print("Shortest distance:", distance, "km")

# calling the function
if __name__ == "__main__":
    display_result("Chitipa", "Blantyre")