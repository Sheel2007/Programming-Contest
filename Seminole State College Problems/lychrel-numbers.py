def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst

number = int(input())
iteration = 0

while True:
    old_number = number

    number_list = [int(x) for x in str(number)]


    if Reverse(number_list) == number_list:
        break

    number_list = Reverse(number_list)

    temp = ""
    number = list(map(str, number_list))
    for num in number:
        temp += num

    number = temp

    iteration += 1

    number = old_number + int(number)

    if iteration >= 10:
        break

print(f'Not a Lychrel number after {iteration} iterations: {number}')
