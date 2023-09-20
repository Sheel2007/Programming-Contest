### Handling Inputs

Many of the VCU questions inputs starts with an integer which dictates the number of times the program will run. The correct way to parse this is:

```python
variable = int(input())
```

Additionally, many problems (for VCU and other competitions) have numbers that are seperated by commas and require you to parse the input. Here is an example of this:

```bash
1 2 3 4 5
```

We are able to parse this using the input().split() method. This will make the input a list. However, notice that the list is made up of strings instead of numbers. To fix this, we use the map() function. 

The map() function takes 2 arguments, a function, and a list. The map function then applies the function to each element of a list. In this case, we use the int() function to convert every string to an integer. Here is how we do this in python:

```python
variable = list(map(int, input().split()))
```

In some (very rare) cases, the problem does not provide a number that specifies the number of times to run your program. In this case we need to use the sys module to loop through every input line provided. Here is the way to do this:

```python
import sys 
  
for variable in sys.stdin: 
    # do stuff with variable
```

Lastly, instead of typing out every single character everytime we need to test our code we can simply redirect the input to a file. 

As an example lets use the Card Shark Problem (Problem A) from the 2013 VCU Set:

Here is the contents of our text file:

```bash
5
1 2 3 4 5 6 7
1 2 3 4 6 7 8
1 2 3 3 4 4 4
11 1 5 4 12 2 3
5 1 3 2 6 7 9
```

Here is the code in our python file:

```python
# Read the number of hands to evaluate
num_hands = int(input())

# Evaluate each hand
for _ in range(num_hands):
    hand = list(map(int, input().split()))
    # do something with the hand variable
```

Notice how the code is structured exactly the same. The only difference will be in how we run the file. Here is how we run the program

```console
python3 main.py < file.txt
```

This will redirect the input of our python file to the text file that we have created. 
