#Ascending Descending order.

ls = []
num = int(input("How many number: "))
for i in range(num):
    numbers = int(input("Enter number: "))

    ls.append(numbers)
    
print("This is numbers in ascending order: " ,sorted(ls))
print("This is numbers in descending order: ",reversed ,sorted(ls))

