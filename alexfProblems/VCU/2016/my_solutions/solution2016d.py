import sys
from typing import TextIO

def fast_distance(cord1, cord2):
    # Computes a number that can be used to compare the lengths of lines
    # abs(x1 - x2) + abs(y1 - y2)
    return abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1])

def fast_area(cord1, cord2, cord3):
    # Computes double the area of a triangle. This number is fine to use when comparing the sizes of triangles.
    return abs(cord1[0] * (cord2[1] - cord3[1]) + cord3[0] * (cord1[1] - cord2[1]) + cord2[0] * (cord3[1] - cord1[1]))

def main(input: TextIO, output: TextIO):
    triangle = list(map(float, input.readline().split(" ")))
    cord1 = (triangle[0], triangle[1])
    cord2 = (triangle[2], triangle[3])
    cord3 = (triangle[4], triangle[5])

    triangle0_area = fast_area(cord1, cord2, cord3)

    total_points = int(input.readline())

    for i in range(0, total_points):
        cord = tuple(map(float, input.readline().split(" ")))
        triangle1_area = fast_area(cord, cord1, cord2)
        triangle2_area = fast_area(cord, cord2, cord3)
        triangle3_area = fast_area(cord, cord3, cord1)

        if (triangle1_area + triangle2_area + triangle3_area) == triangle0_area:
            output.write("1\n")
        else:
            output.write("0\n")

if __name__ == "__main__":
    main(sys.stdin, sys.stdout)