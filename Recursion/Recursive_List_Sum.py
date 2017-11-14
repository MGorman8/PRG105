# M Gorman
# 12.2 Recursive list sum


# main function
def main():
    # list of numbers
    numbers = [2, 4, 6, 8, 10]

    # call range_sum function using numbers list, starting at first index, ending at last index
    my_sum = range_sum(numbers, 0, 4)

    # display results
    print('The sum of my list of numbers is: ', my_sum)


# range_sum function
def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

main()
