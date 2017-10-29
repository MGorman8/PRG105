# Mike Gorman
# 8.2 Alphabetic Telephone Number Translator


def main():
    # intro
    print('Welcome to the \'Wordy\' phone number converter.')
    print('I will take your phone number with letters in it and convert it to plain numbers.')
    # get user input
    phone = input('Please enter the 10 digit phone number as XXX-XXX-XXXX.: ')
    # convert input into all caps
    big_phone = phone.upper()
    # blank string for converted number storage
    new_phone = ''
    # for loop to run through phone number one digit/letter at a time and run conversion function
    for i in big_phone:
        # get x from convert function - send i to convert function and run convert()
        x = convert(i)
        # add converted digit/letter to converted number
        new_phone += x
    # print results
    print('Your converted phone number is: ' + new_phone)


# definition of convert function - get i from for loop in main
def convert(i):
    # if statements to convert i to numeric value if an alpha character
    if i == '-' or i == '/' or i == '\\' or i == ' ':
        x = '-'
    if i.isdigit():
        x = str(i)
    if i == 'A' or i == 'B' or i == 'C':
        x = str(2)
    if i == 'D' or i == 'E' or i == 'F':
        x = str(3)
    if i == 'G' or i == 'H' or i == 'I':
        x = str(4)
    if i == 'J' or i == 'K' or i == 'L':
        x = str(5)
    if i == 'M' or i == 'N' or i == 'O':
        x = str(6)
    if i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        x = str(7)
    if i == 'T' or i == 'U' or i == 'V':
        x = str(8)
    if i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        x = str(9)
    # print(x) # test code
    # send x (converted value) back to main to be placed into final phone number
    return x

# call main
main()

