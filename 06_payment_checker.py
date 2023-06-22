# functions go here 6

# checks if user enters a payment method
def cash_credit(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("Please choose a valid payment method")

# main routine goes here

want_instructions = cash_credit("Choose a payment method (cash or credit): ")

if want_instructions == "yes":
    print("Instructions go here")

print("program continues...")
print()
