#Cheak if a number is positive, negative or 0..

a = input("Enter your number: ")
a = int(a)

if a < 0:
    print("This is a negative number. ")
elif a > 0:
    print("This is a positive number")
else:
    print("This is zero. ")
    