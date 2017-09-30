#  Mike Gorman
#  5.2 Automobile costs


#  function 1 - get monthly information
def month():
    #  get car payment
    note = float(input('What is the monthly car payment? : $'))
    #  get insurance amount
    insurance = float(input('How much do you pay for car insurance each month? : $'))
    #  get fuel costs
    gas = float(input('What is your average monthly fuel cost? : $'))
    #  get total monthly cost
    monthly_cost = note + insurance + gas
    #  print monthly cost
    print('You spend about $' + format(monthly_cost, ',.2f'), 'for your car a month.')
    #  pass monthly_cost into year() and call year()
    year(monthly_cost)


#  function 2 - get yearly costs
def year(monthly_cost):
    yearly_cost = float(monthly_cost * 12)
    print('Your yearly cost to own your car is $' + format(yearly_cost, ',.2f') + '.')

#  call month()
month()

