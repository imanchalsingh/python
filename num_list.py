start_num = int(input("Enter start number: "))
end_num = int(input("Enter last number: "))

ls = []

#Check if number is even number and divisible by (3 and 7)
for i in range(start_num, end_num+1):
    if i%2==0:
        if i%3==0 and i%7==0:
            ls.append(i)
            
print("List is : ", *ls)