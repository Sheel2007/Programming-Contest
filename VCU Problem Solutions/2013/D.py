def get_tickets(ticket_start, index, num_tickets):
    global tickets, count
    solution, temp = [], []
    temp.append(ticket_start)
    for idx, ticket in enumerate(tickets):
        if not idx <= index and not ticket <= ticket_start:
            temp.append(ticket)

    for j in range(1, num_tickets):
        for i in range(1, num_tickets - 1):
            try:
                if tickets[index + i] > tickets[index] and tickets[index + i + j] > tickets[index + i]:
                    solution.append([tickets[index], tickets[index + i], tickets[index + i + j]])
            except:
                continue

    # remove duplicated from list 
    result = [] 
    for i in solution: 
        if i not in result: 
            result.append(i)

    count += len(result)
    
num_tickets = int(input())
tickets = list(map(int, input().split()))
count = 0

for index, ticket in enumerate(tickets):
    get_tickets(ticket, index, num_tickets)

print(count)