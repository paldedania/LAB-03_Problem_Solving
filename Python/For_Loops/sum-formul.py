# Sum from 1 to N
# Take n from the user and calculate:


number=int(input("Enter a number: "))
sum = 0
for i in range(1,(number+1)):
    sum+=i
print(sum)