# Problem E from https://egr.vcu.edu/media/engineering/documents/cs/VCU_HSContest_2016_Problems.pdf
import sys

from typing import TextIO

def main(input: TextIO, output: TextIO) -> None:
    protein1: str = input.readline().strip()
    protein2: str = input.readline().strip()

    if len(protein1) > len(protein2):
        short_length: int = len(protein2)
    else:
        short_length: int = len(protein1)

    number_same_acids: int = 0
    for i in range(0, short_length):
        if protein1[i] == protein2[i]:
            number_same_acids += 1

    output.write(f"{number_same_acids}/{short_length}\n")

if __name__ == "__main__":
    main(sys.stdin, sys.stdout)