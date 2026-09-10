#Find the LCM of two numbers.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
for i in range(num1,num1*num2+1):
    if i%num1==0 and i%num2==0:
        lcm=i
        break
print(lcm)        