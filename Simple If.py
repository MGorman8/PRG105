# Variable
x = int(input("Enter a number between 1 and 7. "))

# If statements
if x == 1:
    print("You have chosen Monday!")
elif x == 2:
    print("You have chosen Tuesday!")
elif x == 3:
    print("You have chosen Wednesday!")
elif x == 4:
    print("You have chosen Thursday!")
elif x == 5:
    print("You have chosen Friday!")
elif x == 6:
    print("You have chosen Saturday!")
elif x == 7:
    print("You have chosen Sunday!")
elif x < 1 or x > 7:
    print("You have failed to choose between 1 and 7!")
