import heapq

def dijkstra(graph, start, end):
    # Priority queue: (distance, node)
    pq = [(0, start)]
    
    # Distances dictionary
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Previous node dictionary (to reconstruct path)
    previous = {node: None for node in graph}
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # Stop if we reach the destination
        if current_node == end:
            break
        
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            
            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct shortest path
    path = []
    node = end
    while node is not None:
        path.insert(0, node)
        node = previous[node]
    
    return distances[end], path


# Example graph: cities as nodes and highways as weighted edges
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 8, 'D': 4},
    'C': {'A': 2, 'B': 8, 'D': 7, 'E': 6},
    'D': {'B': 4, 'C': 7, 'E': 3, 'F': 5},
    'E': {'C': 6, 'D': 3, 'F': 1},
    'F': {'D': 5, 'E': 1}
}

start_city = 'A'
end_city = 'F'

distance, path = dijkstra(graph, start_city, end_city)
print(f"Shortest distance from {start_city} to {end_city}: {distance}")
print(f"Path: {' -> '.join(path)}")