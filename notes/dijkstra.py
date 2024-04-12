def dijkstra(graph, start):
    """
    Dijkstra's algorithm to find the shortest paths from a starting node to all other nodes in a weighted graph.

    Args:
    - graph: The graph represented as a dictionary where keys are nodes and values are dictionaries of neighboring nodes and their corresponding edge weights.
    - start: The starting node.

    Returns:
    - shortest_paths: A dictionary where keys are nodes and values are the shortest distances from the start node to each node.
    """
    # Initialize a dictionary to store the shortest distances from start to each node
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0  # Distance from start to itself is 0

    unvisited_nodes = set(graph.keys())  # Set of unvisited nodes

    while unvisited_nodes:
        # Find the unvisited node with the smallest tentative distance
        current_node = min(unvisited_nodes, key=lambda node: shortest_paths[node])

        # Remove the current node from unvisited nodes
        unvisited_nodes.remove(current_node)

        # Explore neighbors of the current node
        for neighbor, edge_weight in graph[current_node].items():
            distance = shortest_paths[current_node] + edge_weight

            # Update shortest distance if a shorter path is found
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance

    return shortest_paths

# Example usage:
graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'C': 1, 'D': 6},
    'C': {'D': 2},
    'D': {}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
# Outputs {'A': 0, 'B': 3, 'C': 4, 'D': 6}
