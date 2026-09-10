# user gives a input we are suppose to make a patter using * in xbyx format

num = int(input("Whats your number: "))

for i in range(0,num):
    for j in range(0,num):
        print("*",end="")
    print()
