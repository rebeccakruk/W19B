from calculators.addition import add
from calculators.subtraction import subtract
from calculators.multiplication import multiply
from calculators.division import divide

is_valid = False
is_calcs = False


calc_choice = int(input("Please select a calculation: 1. Add, 2. Subtract, 3. Multiply, 4. Divide "))

# if calc_choice == int and calc_choice <1 and calc_choice >4:
#         is_valid = True

# elif calc_choice not in range(1-4):
#         print("Out of range. Please select a number between 1 - 4")
# elif calc_choice != int or calc_choice not in range(1,4):
#         print("You entered something that isn't a number. Please select a number between 1 - 4")

#         if (is_valid):
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


            # is_calcs = True

        # print("You entered something that isn't a number. Please select a number")

        
