# M Gorman
# 12.1 Recursive_Printing

# Design a recursive function that accepts one integer argument, n, and prints the numbers 1 up through n.


# main
def main():
    n = int(input('Please enter an integer for the number you wish to count to. :'))
    count(n)


# count function
def count(number):
    if number > 0:
        count(number - 1)
        print(number)
main()
