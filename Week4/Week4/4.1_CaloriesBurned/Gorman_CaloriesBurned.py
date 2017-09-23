'''
M Gorman
4.1 Calories Burned
'''

#Variable
calorie = float(4.2)  # calories burned in 1 minute

for minutes in range(10, 35, 5):  # for loop with variable for minutes in range (start, stop, interval)
    cals = float(calorie * minutes)  # cals = calorie * minutes
    print('The calories burned in', minutes, 'minutes are:', cals)
