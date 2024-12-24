#Calculator............

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
operator = input("Enter Operator (+,-,/,*,%): ")

first_number = int(first_number)
second_number = int(second_number)

if operator == "+":
    print(first_number+second_number)
elif operator == "-":
    print(first_number-second_number)
elif operator == "/":
    print(first_number/second_number)
elif operator == "*":
    print(first_number*second_number)
elif operator == "%":
    print(first_number%second_number)
else:
    print("There is no operator")
