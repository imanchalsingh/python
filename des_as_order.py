#Ascending Descending order.

ls = []
num = int(input("How many number: "))
for i in range(num):
    numbers = int(input("Enter number: "))

    ls.append(numbers)

ls.sort()  
print("This is numbers in ascending order: " ,ls)

ls.reverse()
print("This is numbers in descending order: ",ls)

