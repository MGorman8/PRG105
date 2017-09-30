# M Gorman
# 5.4 Calories by macronutrient


# Global variable for cumulative total
total = float(0)


# Function for fat
def fat():
    global total
    fat_grams = float(input('How many grams of fat did you eat? :'))
    fat_cals = fat_grams * 9
    print('You ate', fat_cals, 'calories from fat.')
    total += fat_cals


# Function for carbohydrates
def carbs():
    global total
    carb_grams = float(input('How many grams of carbohydrates did you eat? :'))
    carb_cals = carb_grams * 4
    print('You ate', carb_cals, 'calories from carbohydrates.')
    total += carb_cals


# Function for protein
def protein():
    global total
    protein_grams = float(input('How many grams of protein did you eat? :'))
    protein_cals = protein_grams * 4
    print('You ate', protein_cals, 'calories from protein.')
    total += protein_cals


# main function
def main():
    global total
    fat()
    carbs()
    protein()
    print('You consumed',format(total, ',.2f'), 'calories.')

# call main
main()
