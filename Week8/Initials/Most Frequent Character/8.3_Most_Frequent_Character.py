# Mike Gorman
# 8.3 Most Frequent Character

# Write a program that lets the user enter a string and displays the LETTER that appears most frequently
#  in the string, ignore spaces, punctuation, and Upper vs Lower case
#
# Use appropriate variables, functions, and comments. Upload your pseudocode as a Word document,
#  and hand in the link to GitHub in the comments.


def main():
    # user input
    start_string = input('What string would you like to play with?: ')
    # convert to upper case
    big_string = start_string.upper()
    # empty list
    char_list = []
    # for loop to fill the list
    for i in big_string:
        if i.isalpha():
            char_list += i
    # add dummy character to end of list for range and comparisons
    char_list.append('z')
    # sort list
    char_list.sort()
    # test code
    # print(char_list)

    # create and initialize variables to hold the most frequent character and for counters
    # start with first character as default largest
    most_char = char_list[0]
    most_count = 1
    char_count = 1
    # for loop to run through the list of characters and compare values
    for j in range(0, len(char_list) - 1):
        if char_list[j] == char_list[j + 1]:
            char_count += 1
        if char_list[j] != char_list[j + 1] and char_count > most_count:
            most_count = char_count
            most_char = char_list[j]
            char_count = 1
        if char_list[j] != char_list[j + 1] and char_count < most_count:
            char_count = 1

    # display results
    print('The character used the most is: ' + most_char)
    print(most_char, 'appears', most_count, 'times.')


main()
