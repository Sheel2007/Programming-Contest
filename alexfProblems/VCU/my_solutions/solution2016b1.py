# Problem B from https://egr.vcu.edu/media/engineering/documents/cs/VCU_HSContest_2016_Problems.pdf
import sys

def main(input, output):
    for line in input:
        if line == "\n": break
        output.write(f"{(int(line[3]) + 5) % 10}{(int(line[2]) + 5) % 10}{(int(line[1]) + 5) % 10}{(int(line[0]) + 5) % 10}\n")

if __name__ == "__main__":
    main(sys.stdin, sys.stdout)