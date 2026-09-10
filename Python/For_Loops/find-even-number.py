# take a input form the user and find even numbers:


number = int(input("Enter number: "))

count = 0

for i in range(1, number + 1):
    if i % 2 == 0:
        count += 1

print("Number of even numbers:", count)