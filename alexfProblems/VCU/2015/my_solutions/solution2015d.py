# Problem D from https://egr.vcu.edu/media/engineering/documents/cs/VCU_HSContest_2015_Problems.pdf
import sys

from typing import TextIO

# typing for tab completion
def main(input: TextIO, output: TextIO):
    line1 = input.readline().split(" ")
    line2 = input.readline().split(" ")

    longest_dolphin = []
    latest_match = 0
    for word1 in line1:
        for i in range(latest_match, len(line2)):
            word2 = line2[i]
            if word1 == word2:
                longest_dolphin.append(word2)
                latest_match = i
                break
    print(longest_dolphin)

if __name__ == "__main__":
    main(sys.stdin, sys.stdout)