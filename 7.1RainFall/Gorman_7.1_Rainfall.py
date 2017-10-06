# Gorman
# 7.1 Rainfall Statistics

# list of months
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
         'October', 'November', 'December']

# list to hold user input for rainfall each month
rainfall = []

# variable to hold total rainfall
total_rain = 0

# for loop to fill rainfall list
for i in range(len(month)):
    print('For the month of', month[i], 'how much rain fell in inches?')
    rain = float(input(': '))
    total_rain += rain
    rainfall.append(rain)

""" loop to make sure list is filled correctly
 for j in range(len(month)):
    print(rainfall[j])
"""
# clear the screen
print('\n'*25)
# variable to hold average
average = total_rain / len(month)
# display average
print('The average rainfall this year was', format(average,',.2f'), 'inches per month.')

# find and display the month with the most and least rain
most = rainfall.index(max(rainfall))
least = rainfall.index(min(rainfall))

print('The month with the most rain was', month[most])
print('The month with the least rain was', month[least])
# move final display up from bottom
print('\n'*8)
