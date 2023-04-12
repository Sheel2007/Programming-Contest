# Problem A from https://egr.vcu.edu/media/engineering/documents/cs/VCU_HSContest_2015_Problems.pdf
import sys

from typing import TextIO

def drop(s: set, i) -> bool: # discards i from the set and returns true if i was discarded successfully otherwise false
    old_len = len(s)
    s.discard(i)
    return old_len != len(s)

# typing for tab completion
def main(input: TextIO, output: TextIO):
    input.readline()
    ids = input.readline()[:-1].split(" ")
    s = set()
    for i in ids:
        if not drop(s, i):
            s.add(i)
    output.write(f"{list(s)[0]}\n")

if __name__ == "__main__":
    main(sys.stdin, sys.stdout)