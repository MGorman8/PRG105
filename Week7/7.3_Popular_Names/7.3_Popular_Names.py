# Mike Gorman
# 7.3 Popular Names


# main function
def main():
    # create lists to hold contents of name files
    boys = []
    girls = []
    # flag variables
    boy_name = False
    girl_name = False

    # open, read, save files to the lists, and close the files
    infile = open('BoyNames.txt', 'r')
    boys = infile.readlines()
    infile.close()
    infile = open('GirlNames.txt', 'r')
    girls = infile.readlines()
    infile.close()

    # strip the new line from the lists
    index = 0
    while index < len(boys):
        boys[index] = boys[index].rstrip('\n')
        index += 1
    index2 = 0
    while index2 < len(girls):
        girls[index2] = girls[index2].rstrip('\n')
        index2 += 1

    # sort the lines
    boys.sort()
    girls.sort()

    # ask for name to search
    name = input('What name would you like to check the popularity of? :')

    # search the lists for user input
    if name in boys:
        boy_name = True
    if name in girls:
        girl_name = True

    # Display results

    if girl_name == True & boy_name == True:
        print('The name you entered is a popular boy and girl name.')
    elif boy_name == True:
        print('That is a popular name for boys.')
    elif girl_name == True:
        print('That name is popular for girls.')
    else:
        print('The name you searched is not a popular name.')

main()


""" # test code
    print(boys)
    print(girls)
    print(boy_name)
    print(girl_name)
"""
