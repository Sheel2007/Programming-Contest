"""
#sample input
MGINTRELFLNFTIVLITVILMWLLVRSYQY
MERSTQELFINFTVVLITVLLMWLLVRSYQY

#sample output

24/31

"""

protein1 = list(input())
protein2 = list(input())

correct = len(protein1)

for i in range(len(protein1)):
	if not protein1[i] == protein2[i]:
		correct -= 1

print(str(correct) + '/' + str(len(protein1)))
