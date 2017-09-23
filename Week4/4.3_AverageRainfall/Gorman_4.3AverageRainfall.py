"""
M Gorman
4.3 Average Rainfall
"""

#  get user input for number of years measured
years = int(input('How many years would you like to get the average rainfall for?: '))
total = float(0.0)  # counter for total rain

for year in range(years):  # year = current year
    for month in range(12):  # month = current month
        print('Year', year + 1, ' month', month + 1)
        # rain = How much rain, in inches, fell in this month?
        rain = float(input('How much rain, in inches, fell in this month?:'))
        total += rain  # add this months rain to total

average = (total/(12 * years))  # divide total by 12 months per year
print('-----------------------------------------------')
print('Over', years, 'years the total rainfall was', (format(total, ',.2f')), 'inches.')
print('The average rainfall per month was', (format(average, ',.2f')), 'inches.')
