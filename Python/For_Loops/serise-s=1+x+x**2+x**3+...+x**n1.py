#Write a program to find sum of the series:
#s=1+x+x**2+x**3+...+x**n
x = float(input("Enter value of x : "))
n = int(input("Enter value of n (for x ** n) : "))
s = 0
for a in range(n + 1):
    s += x ** a
print("Sum of first", n, "terms :", s)
