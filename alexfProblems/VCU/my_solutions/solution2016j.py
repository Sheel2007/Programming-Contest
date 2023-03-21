# Problem J from https://egr.vcu.edu/media/engineering/documents/cs/VCU_HSContest_2016_Problems.pdf
import sys
import math

def main(input, output):
    number_problems = int(input.readline())

    for i in range(0, number_problems):
        parameters = list(map(int, input.readline().split(" ")))
        E = parameters[0]
        p = parameters[1]
        R = parameters[2]
        Y = parameters[3]

        number_males = E
        number_females = E
        # Compute a number from 0 to 1 that is the percentage of rabbits that survive each generation, this is an easier number to work with
        survivor_rate = 1 - (p/100)
        # Compute the number of males born to each female in a generation
        male_births = math.floor(R / 2)
        # Compute the number of females born to each female in a generation
        female_births = math.ceil(R / 2)

        for i in range(0, Y - 1):
            # AI Winter
            number_males = math.floor(number_males * survivor_rate)
            number_females = math.floor(number_females * survivor_rate)
            # Spring
            number_males += number_females * male_births
            number_females += number_females * female_births
        
        output.write(f"{number_males + number_females}\n")

if __name__ == "__main__":
    main(sys.stdin, sys.stdout)