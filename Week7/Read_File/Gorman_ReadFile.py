#  Mike Gorman
#  6.1 Read File


def main():

    #  variable to open and hold file contents(file name, r for read)
    input_file = open('names.txt', 'r')
    #  variable to count the names
    num_names = 0
    #  get the first line
    record = input_file.readline()
    #  remove the \n
    record = record.rstrip('\n')
    #  while loop to print and count names in file
    while record !="":
        print(record)
        record = input_file.readline()
        record = record.rstrip('\n')
        num_names += 1
    input_file.close()
    print('There are ', num_names, 'names in the file.')
main()
