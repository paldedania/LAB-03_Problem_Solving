# write an python program to print fibonacci series first 20 elements.Some initial elements of a fibonacci series are:0 1 1 2 3 5 8....

first=0
second=1
print(first)
print(second)
for a in range(1,19):
    third=first+second
    print(third)
    first,second=second,third