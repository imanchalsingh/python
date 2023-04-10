#This program is for getting Bank FD.
name=input("Enter your Name: ")
name1=input("Enter your father name: ")
ac=input("Enter your gmail id: ")
num=input("Enter your mobile number: ")
ac_no=input("Enter your account number(last 4 digit): ")
print("\nCongratulations! Now your account connect our bank.")

# import random
# x=random.randint(10000000000000,99999999999999)
# print("\nGive us some more information for getting bank FD.")

print("\nThis is the information of FD.")
print("For 1 year == Benefit 5%")
print("For 3 year == Benefit 10%")
print("For 5 year == Benefit 20%")
print("For 10 year == Benefit 35%")
print("For 20 year == Benefit 50%")

fd_ac=int(input("\nHow much amount you want to deposit: "))
year_fd=int(input("For how many years you want to deposit the amount: "))

add = int (fd_ac * year_fd) / 100;
print(add)
print("Your received amount is:-")
rec=int(fd_ac + add)
print(rec)

print("\nThank You!")