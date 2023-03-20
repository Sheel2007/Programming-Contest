def manhattan(l1,l2, d):
    total = 0
    for i in range(d):
        v1 = l1[i]
        v2 = l2[i]
        total += abs(v1-v2)
    return total

for z in Zs:

    distances = []
    for neighbor in neighbors:
        distances.append(manhattan(neighbor, z, dimensions))
    
    values = []

    for k in range(K):
        
        i = 0
        lowest_i = 0
        lowest = distances[0]
        for distance in distances:
            if distance < lowest:
                lowest = distance
                lowest_i = i
        values.append(neighbors[i][-1])

    mappedValues = range(max(values))
    
    for value in values:
        mappedValues[value] += 1
    print(mappedValues.index(max(mappedValues)))
