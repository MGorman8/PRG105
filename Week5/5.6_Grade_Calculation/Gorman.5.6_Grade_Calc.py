# M Gorman
# 5.6 Grade Calculation


# calc_average function - get, store, average out scores
def calc_average():
    score1 = float(input('What is the score for the first test? :'))
    score2 = float(input('What is the score for the second test? :'))
    score3 = float(input('What is the score for the third test? :'))
    score4 = float(input('What is the score for the fourth test? :'))
    score5 = float(input('What is the score for the fifth test? :'))
    average = (score1 + score2 + score3 + score4 + score5)/5
    # call and pass average into determine_grade()
    determine_grade(average)


# determine_grade function
def determine_grade(average):
    if (average >= 90):
        grade = 'A'
    elif (average < 90 and average >= 80):
        grade = 'B'
    elif (average < 80 and average >= 70):
        grade = 'C'
    elif (average < 70 and average >= 60):
        grade = 'D'
    else:
        grade = 'F'
    # convert average to string for output
    string_average = str(average)
    # blank line then final output
    print()
    print('Your average test score was', string_average + '.')
    print('Your final grade is a', grade + '.')


calc_average()
