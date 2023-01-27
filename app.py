from calculators.addition import add
from calculators.subtraction import subtract
from calculators.multiplication import multiply
from calculators.division import divide

is_valid = False

while not is_valid:
    calc_choice = input("Please select a calculation: 1. Add, 2. Subtract, 3. Multiply, 4. Divide ")
    try:
        calc_choice = int(calc_choice)
        is_valid = True
    except ValueError:
        print("You entered something that isn't a number. Please select a number between 1 - 4")
# I couldn't get the range to work :(
    # except IndexError:
    #     int(calc_choice <0 and calc_choice >5)
    #     print("Out of range. Please enter a number between 1 - 4")
    else:
        num_one = int(input("Enter first number: "))
        num_two = int(input("Enter second number: "))

if calc_choice == 1:
    print("{} + {}".format(num_one,num_two))
    add(num_one, num_two)

elif calc_choice == 2:
    print("{} - {}".format(num_one,num_two))
    subtract(num_one, num_two)

elif calc_choice == 3:
    print("{} x {}".format(num_one,num_two))
    multiply(num_one, num_two)

elif calc_choice == 4:
    print("{} / {}".format(num_one,num_two))
    divide(num_one, num_two)

