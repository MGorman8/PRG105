# Variable
age = float(input("What is the age of the person you want to classify? :"))

# Main
if age <= 1.0:
    print("This person is an infant.")
elif age > 1.0 and age < 13.0:
    print("This person is a child.")
elif age >= 13.0 and age < 20.0:
    print("This person is a teenager.")
else:
    print("This person is an adult.")
