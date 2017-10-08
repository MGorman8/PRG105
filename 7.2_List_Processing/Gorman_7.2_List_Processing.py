#  M Gorman
#  7.2 List Processing

#  imports
import random

#  empty list
numbers = []
choice = 0


#  function to create list of 20 random integers
def number_list():
# tell function to use global list
    global numbers
# fill empty list
    for i in range(0, 20, 1):
        x = random.randint(1, 99)
#  check for duplicates
        for j in range(len(numbers)):
            if x == numbers[j]:
                x = random.randint(1, 99)
#  assign number to list
        numbers.append(x)
#  sort list
    numbers.sort()


#  function to get and validate user input
def guess():
    # force user to enter a NUMBER
    while True:
        try:
            guess = float(input('Enter a number between 1 and 100. :'))
        except ValueError:
            print("you must enter a number")
            continue
        else:
            break
#  force user to enter a VALID NUMBER
    while guess < 1 or guess > 100:
        while True:
            try:
                guess = float(input('Enter a number between 1 and 100. :'))
            except ValueError:
                print("you must enter a number")
                continue
            else:
                break
#  tell function to use global variable and assign user input to the global variable
    global choice
    choice = guess


# function to test data and display results
def test():
    # check if user number is greater than the largest number in the list
    if choice > numbers[19]:
        print('Your number is higher than every number in the list.')
    # if user number is NOT greater than the largest number in the list..print the part of list
        # that is larger
    else:
        print('The following numbers in the list are higher than your number: ')
        for n in range(len(numbers)):
            if choice < numbers[n]:
                print(numbers[n])


#  Call functions
number_list()
guess()
test()


"""
#  test code
print(choice)
for j in range(len(numbers)):
    print(numbers[j])
"""
