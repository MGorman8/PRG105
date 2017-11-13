# M Gorman
# 10.1 Personal Information Class

# Design a class that holds the following personal data: name, address, age, and phone number.
# Write appropriate accessor and mutator methods (get and set). Also, write a program that
# creates three instances of the class. One instance should hold your information and the other
# two should hold information you make up.  Just add information, don't get it from the user.


# Class
class PersonData:
    # initializer/Constructor
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    # getter/accessor
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone

    # setter/mutator
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone(self, phone):
        self.phone = phone

    # display function
    def display_data(self):
        print('Name:   ', self.get_name(), '\nAddress:', self.get_address(),
              '\nAge:    ', self.get_age(), '\nPhone:  ', self.get_phone(),'\n')


# main function
def main():
    # call 3 objects of class PersonalData with pre-populated attributes
    jim = PersonData('Jim', '22 W. Hope St.', 45, '815-444-3333')
    sara = PersonData('Sara', '532 N. Executor Ln.', 34, '815-555-1239')
    mike = PersonData('Mike', '2808 Stilling Blvd.', 36, '815-679-8416')

    # call display_data function for each object
    jim.display_data()
    sara.display_data()
    mike.display_data()


#call main()
main()
