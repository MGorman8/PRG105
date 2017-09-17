#intro
print("Welcome to the Smaug Phone Service bill helper.")
print("We offer 3 phone packages to choose from.")
print("Package A costs $39.99 and offers 450 minutes a month and $0.45 per additional minute.")
print("Package B costs $59.99 and offers 900 minutes a month and $0.40 per additional minute.")
print("Package C costs $69.99 and offers unlimited minutes a month.")

# Variable
package = input("Which package do you have? A, B, or C?")
# validation
if package != 'A' and package != 'B' and package != 'C' and package != 'a' and package != 'b' and package != 'c':
    print("You have chosen an incompatible package, prepare to be eaten.")
    quit()

# determine bill
elif package == 'a' or package == 'b' or package == 'A' or package == 'B':
    minutes = float(input("How many minutes did you use?")) # minutes and extra variables for total bill determination
    if package == 'a' or package == 'A':
        extra = (minutes - 450)
        if extra > 0:
            total = 39.99 + (extra * .45)
            print("Your bill this month is $", (format(total, ',.2f')))
        else:
            print("Your bill is $39.99.")
    elif package == 'b' or package == 'B':
        extra = (minutes - 900)
        if extra > 0:
            total = 59.99 + (extra * .40)
            print("Your bill this month is $", (format(total, ',.2f')))
        else:
            print("Your bill is $59.99.")

else:
    print("You have package C so your bill is $69.99.")

