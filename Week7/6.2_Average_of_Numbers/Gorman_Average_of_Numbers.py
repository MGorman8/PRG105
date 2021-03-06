#  M Gorman
#  6.2_Average_of_Numbers


def main():
    # accumulator variable
    total = 0
    # counter variable
    counter = 0
    # open file numbers.txt
    infile = open('numbers.txt', 'r')
    # loop to read the values
    for line in infile:
        amount = float(line)
        total += amount
        counter += 1

    # close file
    infile.close()
    # print output
    print('There were', counter, 'numbers.')
    print('The total is', format(total, ',.2f'))
    print('The average of the numbers is ', format(total/counter, ',.2f'), sep='')

# call main
main()
