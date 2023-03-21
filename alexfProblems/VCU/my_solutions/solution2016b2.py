# Problem B from https://egr.vcu.edu/media/engineering/documents/cs/VCU_HSContest_2016_Problems.pdf
import sys

from typing import TextIO

lookup_table = {
    "0" : "5",
    "1" : "6",
    "2" : "7",
    "3" : "8",
    "4" : "9",
    "5" : "0",
    "6" : "1",
    "7" : "2",
    "8" : "3",
    "9" : "4"
}

# typing for tab completion
def main(input: TextIO, output: TextIO):
    for line in input:
        output.write(f"{lookup_table[line[3]]}{lookup_table[line[2]]}{lookup_table[line[1]]}{lookup_table[line[0]]}\n")

if __name__ == "__main__":
    main(sys.stdin, sys.stdout)