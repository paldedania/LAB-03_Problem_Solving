#  user gives a number we have to find its factorial

num = int(input("Which numbers factorial you want: "))
factorial= 1
for i in range(1,num+1):
    factorial *=i

print(f"factorial of {num} is {factorial}")
