# Python script to test my solutions
# Command line arguments:
# Argument 1: mandatory, location of the solution to test
# Argument 2: optional, location of test inputs if not provided stdin is used
# Argument 3: optional, location to put solution output if not provided stdout is used
# Argument 4: optional, location of file to test output against if not provided output is not tested
import sys

from typing import TextIO

solution_path = sys.argv[1]
try:
    input_path = sys.argv[2]
except IndexError:
    input_path = ""
try:
    my_output_path = sys.argv[3]
except IndexError:
    my_output_path = ""
try:
    valid_output_path = sys.argv[4]
except IndexError:
    valid_output_path = ""

def main(input, output): pass # Keep Pylance happy
exec(f"from {solution_path.replace('.py', '').replace('/', '.')} import main") # import main

if input_path != "":
    input_file = open(input_path, "r")
else:
    input_file = sys.stdin
if my_output_path != "":
    output_file = open(my_output_path, "w")
else:
    output_file = sys.stdout

main(input_file, output_file)
input_file.close()
output_file.close()

if valid_output_path != "":
    my_solution_output = open(my_output_path, "r")
    valid_output = open(valid_output_path, "r")
    line_number = 0
    while True:
        line_number += 1
        my_solution_output_line = my_solution_output.readline().replace("\n", "")
        valid_output_line = valid_output.readline().replace("\n", "")

        if my_solution_output_line == "" or valid_output_line == "":
            break

        if my_solution_output_line == valid_output_line:
            print(f"Line {line_number} valid")
        else:
            print(f"Line {line_number} invalid")