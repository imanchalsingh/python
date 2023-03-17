ls = []
num = int(input("How many numbers in list: "))

for i in range(num):
    numbers = int(input("Enter number: "))
    
    ls.append(numbers)
    
print("This is max number in list: " ,max(ls)) 
print("This is min number in list: " ,min(ls))