#A Mersenne prime is a prime number that is equal to two raised to a power minus one (\(2^n - 1\))
#number in the form of (\(2^n - 1\)) are called mersenne number ,eg-(\(2^1 - 1\))=1,(\(2^2 - 1\))=2,(\(2^3 - 1\))=7.......
#Q=write a python program that display first 10 mersenne numbers.

print("First 10 mersenne numbers:")
for a in range(1,11):
    mersenne=2**a-1
    print(mersenne,end=" ")
print()
