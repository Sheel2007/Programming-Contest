# Problem A from https://egr.vcu.edu/media/engineering/documents/cs/VCU_HSContest_2016_Problems.pdf
import sys

from typing import TextIO

def fast_distance(list1, list2, dimensions):
    # Computes a number that can be used when needed to check if distances are larger or smaller but without actually computing the distance. Turns out this is called Manhattan distance.
    # abs(x1 - x2) + abs(y1 - y2) + ... + abs(n1 - n2)
    distance_sum = 0
    for x in range(0, dimensions):
        n1 = list1[x]
        n2 = list2[x]
        distance_sum += abs(n1 - n2)
    return distance_sum

# I've added to typing for tab completion
def main(input: TextIO, output: TextIO):
    parameters = input.readline().split(" ")
    number_known_objects = int(parameters[0])
    number_unknown_objects = int(parameters[2])
    number_dimensions = int(parameters[1])
    k_value = int(parameters[3]) # K value is the number of neighbors to track

    known_objects = []
    while len(known_objects) < number_known_objects:
        line = list(map(float, input.readline()[:-1].split(" ")))
        known_objects.append(line)
    unknown_objects = []
    while len(unknown_objects) < number_unknown_objects:
        line = list(map(float, input.readline()[:-1].split()))
        unknown_objects.append(line)

    for unknown_object in unknown_objects:
        close_objects = []
        for known_object in known_objects:
            distance = fast_distance(known_object, unknown_object, number_dimensions)


if __name__ == "__main__":
    main(sys.stdin, sys.stdout)