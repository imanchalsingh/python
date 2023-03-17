#calculator in python.

first_number = input("enter your first number: " )
second_number = input("enter yuor second number: ")
operator = input("enter operator (+,-,*,/,%) :")

first_number = int(first_number)
second_number = int(second_number)

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    print(first_number / second_number)
elif operator == "%":
    print(first_number % second_number)
else:
    print("There is no operator")


print("Thank you for using.")