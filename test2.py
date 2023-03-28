import sys
import math

# read input values
X, Y, Z, K = map(int, input().split())

# read known objects
objects = []
for i in range(X):
    object = list(map(float, input().split()))
    objects.append(object)

# read unknown objects
unknown_objects = []
for i in range(Z):
    object = list(map(float, input().split()))
    unknown_objects.append(object)

# classify unknown objects
for unknown_object in unknown_objects:
    # calculate distance between unknown object and each known object
    distances = []
    for object in objects:
        distance = math.sqrt(sum([(unknown_object[j] - object[j])**2 for j in range(Y)]))
        distances.append((distance, object[-1]))
    
    # sort distances in ascending order
    distances.sort()
    
    # select the k nearest neighbors
    nearest_neighbors = distances[:K]
    
    # determine the predicted class of the unknown object
    class_counts = {}
    for neighbor in nearest_neighbors:
        if neighbor[-1] not in class_counts:
            class_counts[neighbor[-1]] = 0
        class_counts[neighbor[-1]] += 1
    
    # choose the class with the highest count, breaking ties by choosing the class with the lowest numerical value in the label
    predicted_class = min(class_counts, key=lambda k: (-class_counts[k], k))
    
    # write predicted class to output
    print(predicted_class)