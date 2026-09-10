#Take n from the user and print an inverted triangle using stars.

n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()