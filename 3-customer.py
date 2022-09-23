#!/usr/bin/python3
'''
    A program that accepts customers' firstnames and lastnames and prints
the list of the newly registered customers at the end of the execution
of the program
'''
confirm = input("Register Customer (Yes/No): ")
confirm = confirm.lower()
customers = []

while (confirm):
    # it keeps printing the prompting until the user enters 'no' or 'n'
    # the Yes/No response is not case sensitive and 'y' and 'n' would do
    # any other response is invalid and the customer's names have to be two
    try:
        if ((confirm == 'y') | (confirm == 'yes')):
            fname, lname = input("Enter Customer Name : ").split()
            customers.append({'first': fname, 'last': lname})
            confirm = input("Register Another Customer (Yes/No): ")
            confirm = confirm.lower()

        elif ((confirm == 'n') | (confirm == 'no')):
            print("\nRegistration closed\n")
            break
        else:
            print("Invalid Entry! Enter 'y' to continue or 'n' to stop\n")
            confirm = input("Register Customer (Yes/No): ")
            confirm = confirm.lower()

    except ValueError:
        print("Please enter customer's first name and last name")
        print("(\"Enter 'no' if you wish to stop\")\n")
        confirm = input("Continue Registration (Yes/No): ")
        confirm = confirm.lower()

# it checks for when the user registered no one or just one or more
if (len(customers) == 0):
    print("YOU DID NOT REGISTER ANY CUSTOMER")
elif (len(customers) == 1):
    for i in customers:
        print(f"YOUR NEWLY REGISTERED CUSTOMER IS:\n"
              f"\t{i['first']} {i['last']}")
else:
    print("YOUR NEWLY REGISTERED CUSTOMERS ARE:")
    for name in customers:
        print(f"{(customers.index(name))+1}. {name['first']} {name['last']}")
