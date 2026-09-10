# user gives a input we are suppose to make a patter using * in xbyy format

num1 = int(input("Whats your first number: "))
num2 = int(input("Whats your second number: "))

for i in range(0,num2):
    for j in range(0,num1):
        print("*",end="")
    print()
