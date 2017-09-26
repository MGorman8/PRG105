# Mike Gorman
# 5.1 How much insurance?


# get cost from user, pass to calc_cost
def main():
    structure_value = float(input('What is the replacement cost of the building you need insured? : $'))
    # call calc_cost function
    calc_cost(structure_value)


# calculate cost of the insurance
def calc_cost(value):
    insurance = value * .8
    print('You should get about $', format(insurance, ',.2f'),'of insurance for your building.')

# call main function
main()
