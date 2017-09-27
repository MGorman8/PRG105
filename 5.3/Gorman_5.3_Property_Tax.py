#  M Gorman
#  5.3


"""A county collects property taxes on the assessment value of property, which is 60 percent of the property's actual
 value. For example, if an acre of land is valued at $10,000, its assessment value is $6,000. The property tax is then
 72 cents for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $43.20.

Write a program that asks for the actual value of a piece of property and displays the assessment value and the property
 tax.

Use meaningful names for your variables and function names. Add at least one comment per function describing what it
 does and what other functions it connects to.

Create two separate functions.

Function 1 should gather information from the user and pass that information to Function 2 which will perform the
calculations and display a meaningful result with proper formatting for currency.

Upload your file to GitHub and hand in the link to the file.
"""


# function to get the assessment value of the property
def assess_value(base_value):
    assessed_value = base_value * 0.6
    calc_tax(assessed_value)


# function to get tax amount
    # divide assessed_value by 100, then multiply by .72
def calc_tax(assessed_value):
    tax = ((assessed_value / 100) * .72)
    print('Your tax amount owed is $', format(tax, ',.2f'), sep='')


# main function will get base property value and pass to assess_value.
def main():
    base_value = float(input('What is the base value of your property? $'))
    assess_value(base_value)


main()
