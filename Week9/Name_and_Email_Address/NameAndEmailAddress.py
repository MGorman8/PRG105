#  M Gorman
#  9.1 Name and Email Address

#  Write a program that keeps names and email addresses in a dictionary as key-value pairs.
#  The program should display a menu that lets the user look up a person's email address,
#  add a new name and email address, change an existing email address, and delete an
#  existing name and email address. The program should take the dictionary and save
#  it to a text file when the user exits the program. Each time the program starts,
#  it should retrieve the dictionary from the file and open it for both reading and writing.

#  Make sure you use separate functions;, upload both the created text file and the
#  program to GitHub. Submit a link to the .py file and add a link to the text file
#  in the comments.


import pickle

# Global constants for menu
LOOK_UP = 1
VIEW_ALL = 2
ADD = 3
CHANGE = 4
DELETE = 5
QUIT = 6


def main():
    try:
        input_file = open('customer_file.dat', 'rb')
        customers = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        print('The file is not found. Please add a customer and then quit to create the file.')
        customers = {}

    # Initialize a variable for the user's choice
    choice = 0

    while choice != QUIT:
        # get the user's menu choice
        choice = menu()

        if choice == LOOK_UP:
            look_up(customers)
        elif choice == VIEW_ALL:
            view(customers)
        elif choice == ADD:
            add(customers)
        elif choice == CHANGE:
            change(customers)
        elif choice == DELETE:
            delete(customers)
        elif choice == QUIT:
            save(customers)


def menu():
    print()
    print('Customer email lookup')
    print('---------------------')
    print('1. Look up a customer')
    print('2. View all customers')
    print('3. Add a new customer')
    print('4. Change an email address')
    print('5. Delete a customer')
    print('6. Quit the program\n')

    # get user input (choice)
    choice = int(input("Enter the number of your choice.: "))
    while choice < 1 or choice > 6:
        choice = int(input("Please enter a valid number.: "))
    return choice


def look_up(customers):
    name = input("Enter your customer\'s name.: ")
    print(customers.get(name, 'No customer by that name.'))


def view(customers):
    print(customers)


def add(customers):
    name = input('Enter your customer\'s name. :')
    email = input('Enter the customer\'s email address.: ')
    if name not in customers:
        customers[name] = email
    else:
        print('That customer already exists.')


def change(customers):
    name = input('Enter your customer\'s name. :')
    if name in customers:
        email = input('Enter the new email address.: ')
        customers[name] = email
    else:
        print('No customer by that name.')


def delete(customers):
    name = input('Enter your customer\'s name. :')
    if name in customers:
        del customers[name]
    else:
        print('No customer by that name.')


def save(customers):
    print('Your customer\'s file has been updated.')
    save_file = open('customer_file.dat', 'wb')
    pickle.dump(customers,save_file)
    save_file.close()


main()
