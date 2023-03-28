import math

def euclidean_distance(a, b):
    """
    Calculate the Euclidean distance between two points a and b
    """
    return math.sqrt(sum([(a[i] - b[i])**2 for i in range(len(a))]))

def classify_knn(known_objects, unknown_objects, k):
    """
    Classify the unknown objects using the K-Nearest Neighbors algorithm with k neighbors
    """
    results = []
    for unknown in unknown_objects:
        # Calculate the distance between the unknown object and all known objects
        distances = [(euclidean_distance(unknown[:-1], known[:-1]), known[-1]) for known in known_objects]
        # Sort the distances by increasing order
        distances.sort()
        # Get the k nearest neighbors
        nearest_neighbors = [d[1] for d in distances[:k]]
        # Count the number of occurrences of each class among the k nearest neighbors
        counts = {}
        for neighbor in nearest_neighbors:
            if neighbor in counts:
                counts[neighbor] += 1
            else:
                counts[neighbor] = 1
        # Find the class with the highest count
        max_count = 0
        max_class = None
        for cls, count in counts.items():
            if count > max_count:
                max_count = count
                max_class = cls
            elif count == max_count and cls < max_class:
                max_class = cls
        results.append(max_class)
    return results

# Read input from standard input
X, Y, Z, K = map(int, input().split())
known_objects = []
for i in range(X):
    known_objects.append(list(map(float, input().split())))
unknown_objects = []
for i in range(Z):
    unknown_objects.append(list(map(float, input().split())))

# Classify the unknown objects using the K-Nearest Neighbors algorithm with K neighbors
results = classify_knn(known_objects, unknown_objects, K)

# Write output to standard output
for result in results:
    print(result)