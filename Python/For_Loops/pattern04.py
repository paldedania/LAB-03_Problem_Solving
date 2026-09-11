#Take n from the user and print a diamond where numbers increase and then decreases.

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        print(j, end="")

    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        print(j, end="")

    print()