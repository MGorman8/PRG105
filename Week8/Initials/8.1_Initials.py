# Mike Gorman
# 8.1 Initials


def main():
    # variable for user input name
    name = input('Please enter your first, middle, and last names. Don\'t forget spaces.: ')
    # variable to convert to all caps
    big_name = name.upper()
    # split string into 3 parts based on spaces
    split_name = big_name.split()

    # variable to hold . as a string
    dot = '.'
    # variables to get and hold first letter of each name with the .
    first = split_name[0][0] + dot
    second = split_name[1][0] + dot
    third = split_name[2][0] + dot
    # combine the initials into one string
    initials = (first + second + third)
    # display the initials
    print(initials)

main()
