def shortest_time_to_drive(nTowns, townX, townY, adj_list):
    
    # Parse the highway information
    for _ in range(nTowns - 1):
        line = input().split()
        speed_limit, town1, distance, town2 = int(line[0]), int(line[1]), int(line[2]), int(line[3])
        adj_list[town1].append((town2, distance, speed_limit))
        adj_list[town2].append((town1, distance, speed_limit))

    # Dijkstra's algorithm
    visited = [False] * nTowns # Create a list to keep track of visited towns, initially all set to False.
    min_time = [float('inf')] * nTowns # Create a list to store the minimum time to reach each town, initially set to infinity.
    min_time[townX] = 0 #Set the min time for the starting town to 0.


    while True: # Start a loop for Dijkstra's algorithm.
        # Find the unvisited town with the minimum time
        min_time_town = float('inf') #make a variable to keep track of the min time among unvisited towns.
        for i in range(nTowns): # loop through all towns
            if not visited[i] and min_time[i] < min_time_town:
                # If the town is unvisited and its min time is less than the current min time, update min_time_town.
                min_time_town = min_time[i]
                current_town = i # Store the index of the town with the current min time.

        if min_time_town == float('inf'):
            # If min_time_town remains infinity, it means there are no more unvisited towns with finite min times.
            break

        visited[current_town] = True # Mark the current_town as visited.

        for neighbor, distance, speed_limit in adj_list[current_town]:
            # Iterate through the neighbors of the current town and their distances and speeds.
            if not visited[neighbor]:  # Check if the neighbor is unvisited.
                travel_time = min_time[current_town] + distance / speed_limit #Calculate the time to reach the neighbor.
                if travel_time < min_time[neighbor]:
                    min_time[neighbor] = travel_time
                # If the calculated time is less than the current minimum time to reach the neighbor, update it.

    return min_time[townY]# Return the minimum time to reach the destination town (townY).

# Parse the first line of input
nTowns, townX, townY = map(int, input().split())
adj_list = [[] for _ in range(nTowns)]

result = shortest_time_to_drive(nTowns, townX, townY, adj_list)
print("{:.1f}".format(result))