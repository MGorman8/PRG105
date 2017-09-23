'''
Gorman
4.2 Pennies for Pay
'''
# intro
print('Congratulations, your boss has hit their head and wants to sign you to new contract!')
print('You will work 14 hour days with no days off.')
print('You will also only be paid 1 penny a day that doubles every day.')
print('The length of the contract is up to you!')

days = int(input('How many days will you work?: '))  # user input for number of days user will work
pay = float(0.01)  # variable to track the days pay
total = float(0.00)  # variable to track $ earned
worked = 1  # variable to track what day it is

print()  # blank line
print('Days worked  |  Amount earned that day')
print('--------------------------------------')
for x in range(days):
    if worked == days:  # 
        print('{:>6}'.format(worked), '      |  $', (format(pay, ',.2f')))
        print()
        print('After', worked, 'you have earned $', (format(total, ',.2f')))
    else:
        print('{:>6}'.format(worked), '      |  $', (format(pay, ',.2f')))
        worked += 1
        pay *= 2
        total += pay
    '''
    '{:>6}'.format() is align right
    '''
