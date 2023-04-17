"""
# sample input

5
1 2 3 4 5
bb zzz
-1
"""

import string

alphabet = list(string.ascii_lowercase)

size = int(input()) #5

sequence = input().split()
sequence = [int(i) for i in sequence] #[1, 2, 3, 4, 5]

original = input()
chars = original.replace(" ", "")
characters = [*chars]


_ = input()

for i in range(size):
	if characters[i] == " ":
		continue
	if sequence[i] + alphabet.index(characters[i]) < len(alphabet):
		letter = alphabet[alphabet.index(characters[i]) + sequence[i]]
		characters[i] = letter

	else:
		val = alphabet.index(characters[i]) + sequence[i] - len(alphabet) - 1
		characters[i] = alphabet[i]

answer = ""
for index in range(len(characters)):
	if original[index] == " ":
		answer += " "
	answer += characters[index]

print(answer)
