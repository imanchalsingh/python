#Check prime number.

num = int(input("Enter your number: "))

if num ==  1:
    print("Is not a prime number.")
if num > 1:
    for i in range(2,num):
        if num % 2 == 0:
            print(num ,"is not prime number.")
            break
    else:
        print(num ,"is prime number.")

    
print("Thank You.")

