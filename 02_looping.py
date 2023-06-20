# main routine starts here

# set maximum number of tickets here
MAX_TICKETS = 3

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'x' to quit: ")

    if name == 'x':
        break

    tickets_sold += 1

# output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations, you have sold all available tickets")
else:
    print("You have sold {} ticket/s. There are now {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))